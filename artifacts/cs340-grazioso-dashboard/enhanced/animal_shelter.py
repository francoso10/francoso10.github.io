"""Enhanced MongoDB CRUD module for the CS 340 Grazioso Salvare Dashboard."""

from __future__ import annotations

import copy
import logging
import os
from typing import Any, Dict, Iterable, List, Optional
from urllib.parse import quote_plus

from pymongo import ASCENDING, MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.errors import PyMongoError


class AnimalShelter:
    """CRUD operations with secure configuration, validation, and RBAC."""

    ALLOWED_FILTER_OPERATORS = {"$and", "$or", "$in", "$gte", "$lte", "$eq"}
    ALLOWED_UPDATE_OPERATORS = {"$set"}

    ROLE_PERMISSIONS = {
        "read": {"read"},
        "editor": {"read", "create", "update"},
        "admin": {"read", "create", "update", "delete", "index"},
    }

    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        *,
        role: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[int] = None,
        db_name: Optional[str] = None,
        collection_name: Optional[str] = None,
        auth_source: Optional[str] = None,
        create_indexes: bool = False,
    ) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.role = (role or os.getenv("MONGO_APP_ROLE", "read")).lower().strip()
        if self.role not in self.ROLE_PERMISSIONS:
            raise ValueError(f"Unsupported application role: {self.role}")

        self.username = username or os.getenv("MONGO_USER")
        self.password = password or os.getenv("MONGO_PASS")
        self.host = host or os.getenv("MONGO_HOST", "localhost")
        self.port = int(port or os.getenv("MONGO_PORT", "27017"))
        self.db_name = db_name or os.getenv("MONGO_DB", "aac")
        self.collection_name = collection_name or os.getenv("MONGO_COLLECTION", "animals")
        self.auth_source = auth_source or os.getenv("MONGO_AUTH_SOURCE", "admin")

        if not self.username or not self.password:
            raise ValueError("MongoDB credentials are not configured.")

        user = quote_plus(self.username)
        pwd = quote_plus(self.password)
        uri = f"mongodb://{user}:{pwd}@{self.host}:{self.port}/?authSource={self.auth_source}"
        self.client: MongoClient = MongoClient(uri, serverSelectionTimeoutMS=5000)
        self.database: Database = self.client[self.db_name]
        self.collection: Collection = self.database[self.collection_name]

        if create_indexes:
            self.ensure_indexes()

    def _require_permission(self, permission: str) -> None:
        if permission not in self.ROLE_PERMISSIONS[self.role]:
            raise PermissionError(
                f"Role '{self.role}' does not have permission for '{permission}' operations."
            )

    @staticmethod
    def _validate_key(key: Any, allowed_operators: Iterable[str]) -> str:
        if not isinstance(key, str) or not key:
            raise ValueError("MongoDB keys must be non-empty strings.")
        if key.startswith("$") and key not in allowed_operators:
            raise ValueError(f"Disallowed MongoDB operator: {key}")
        if not key.startswith("$") and ("$" in key or "." in key or "\x00" in key):
            raise ValueError(f"Unsafe MongoDB field name: {key}")
        return key

    @classmethod
    def _sanitize_value(cls, value: Any, allowed_operators: Iterable[str]) -> Any:
        if isinstance(value, dict):
            return cls._sanitize_document(value, allowed_operators)
        if isinstance(value, list):
            return [cls._sanitize_value(item, allowed_operators) for item in value]
        return value

    @classmethod
    def _sanitize_document(
        cls, document: Dict[str, Any], allowed_operators: Iterable[str]
    ) -> Dict[str, Any]:
        if not isinstance(document, dict):
            raise ValueError("MongoDB query and document inputs must be dictionaries.")
        sanitized: Dict[str, Any] = {}
        for key, value in document.items():
            safe_key = cls._validate_key(key, allowed_operators)
            sanitized[safe_key] = cls._sanitize_value(value, allowed_operators)
        return sanitized

    @classmethod
    def sanitize_filter(cls, query: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        if query is None:
            return {}
        return cls._sanitize_document(copy.deepcopy(query), cls.ALLOWED_FILTER_OPERATORS)

    @classmethod
    def sanitize_insert_document(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        return cls._sanitize_document(copy.deepcopy(data), allowed_operators=set())

    @classmethod
    def sanitize_update_document(cls, update_data: Dict[str, Any]) -> Dict[str, Any]:
        sanitized = cls._sanitize_document(
            copy.deepcopy(update_data), cls.ALLOWED_UPDATE_OPERATORS
        )
        if not sanitized or any(operator not in cls.ALLOWED_UPDATE_OPERATORS for operator in sanitized):
            raise ValueError("Only explicit $set updates are allowed.")
        return sanitized

    def ensure_indexes(self) -> List[str]:
        self._require_permission("index")
        return [
            self.collection.create_index([("breed", ASCENDING)], name="idx_breed"),
            self.collection.create_index([("animal_type", ASCENDING)], name="idx_animal_type"),
            self.collection.create_index([("sex_upon_outcome", ASCENDING)], name="idx_sex_outcome"),
            self.collection.create_index([("age_upon_outcome_in_weeks", ASCENDING)], name="idx_age_weeks"),
            self.collection.create_index(
                [
                    ("animal_type", ASCENDING),
                    ("breed", ASCENDING),
                    ("sex_upon_outcome", ASCENDING),
                    ("age_upon_outcome_in_weeks", ASCENDING),
                ],
                name="idx_rescue_filters",
            ),
        ]

    def create(self, data: Dict[str, Any]) -> bool:
        self._require_permission("create")
        try:
            self.collection.insert_one(self.sanitize_insert_document(data))
            return True
        except PyMongoError:
            return False

    def read(self, query: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        self._require_permission("read")
        try:
            return list(self.collection.find(self.sanitize_filter(query)))
        except PyMongoError:
            return []

    def update(self, query: Dict[str, Any], update_data: Dict[str, Any]) -> int:
        self._require_permission("update")
        result = self.collection.update_many(
            self.sanitize_filter(query), self.sanitize_update_document(update_data)
        )
        return result.modified_count

    def delete(self, query: Dict[str, Any]) -> int:
        self._require_permission("delete")
        result = self.collection.delete_many(self.sanitize_filter(query))
        return result.deleted_count
