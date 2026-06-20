package contactservice;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

/**
 * Service layer that manages Contact records.
 * Provides O(1) primary lookup by contact ID and O(log n) sorted access
 * by last-name prefix using a dual-index data structure.
 */
public class ContactService {

    // HashMap: O(1) average-case for ID-based operations.
    private final Map<String, Contact> primaryIndex = new HashMap<>();

    // TreeMap: O(log n) ordered lookup by normalized last name.
    // Values contain IDs rather than Contact objects to avoid stale references.
    private final TreeMap<String, List<String>> secondaryIndex = new TreeMap<>();

    /**
     * Adds a contact to both indexes.
     * Time complexity: O(log n), dominated by TreeMap insertion.
     */
    public void addContact(Contact contact) {
        if (contact == null) {
            throw new IllegalArgumentException("Contact must not be null.");
        }

        String id = contact.getContactId().trim();
        if (primaryIndex.containsKey(id)) {
            throw new IllegalArgumentException("Contact ID already exists: " + id);
        }

        primaryIndex.put(id, contact);
        String nameKey = contact.getLastName().toLowerCase();
        secondaryIndex.computeIfAbsent(nameKey, k -> new ArrayList<>()).add(id);
    }

    /**
     * Removes a contact from both indexes.
     * Time complexity: O(log n) plus O(k) for the list of matching last names.
     */
    public void deleteContact(String contactId) {
        String id = validateId(contactId);
        Contact contact = requireContact(id);

        primaryIndex.remove(id);
        String nameKey = contact.getLastName().toLowerCase();
        List<String> ids = secondaryIndex.get(nameKey);
        if (ids != null) {
            ids.remove(id);
            if (ids.isEmpty()) {
                secondaryIndex.remove(nameKey);
            }
        }
    }

    /**
     * Updates one or more fields of a contact. Passing null leaves that field unchanged.
     * The secondary index is updated if the last name changes.
     */
    public void updateContact(String contactId,
                              String firstName,
                              String lastName,
                              String phone,
                              String address) {
        String id = validateId(contactId);
        Contact contact = requireContact(id);

        if (lastName != null) {
            String oldKey = contact.getLastName().toLowerCase();
            contact.setLastName(lastName);
            String newKey = contact.getLastName().toLowerCase();

            if (!oldKey.equals(newKey)) {
                List<String> oldList = secondaryIndex.get(oldKey);
                if (oldList != null) {
                    oldList.remove(id);
                    if (oldList.isEmpty()) {
                        secondaryIndex.remove(oldKey);
                    }
                }
                secondaryIndex.computeIfAbsent(newKey, k -> new ArrayList<>()).add(id);
            }
        }

        if (firstName != null) {
            contact.setFirstName(firstName);
        }
        if (phone != null) {
            contact.setPhone(phone);
        }
        if (address != null) {
            contact.setAddress(address);
        }
    }

    /**
     * Retrieves a contact by ID in O(1) average time.
     */
    public Contact getContact(String contactId) {
        return requireContact(validateId(contactId));
    }

    /**
     * Returns contacts whose last name begins with the requested prefix.
     * Time complexity: O(log n + k), where k is the number of matches.
     */
    public List<Contact> searchByLastName(String prefix) {
        if (prefix == null || prefix.isBlank()) {
            throw new IllegalArgumentException("Search prefix must not be null or blank.");
        }

        String lo = prefix.toLowerCase();
        String hi = lo.substring(0, lo.length() - 1)
                + (char) (lo.charAt(lo.length() - 1) + 1);

        Map<String, List<String>> range = secondaryIndex.subMap(lo, hi);
        List<Contact> results = new ArrayList<>();
        for (List<String> ids : range.values()) {
            for (String id : ids) {
                Contact contact = primaryIndex.get(id);
                if (contact != null) {
                    results.add(contact);
                }
            }
        }
        return Collections.unmodifiableList(results);
    }

    /**
     * Returns the number of contacts in O(1) time.
     */
    public int size() {
        return primaryIndex.size();
    }

    private String validateId(String contactId) {
        if (contactId == null || contactId.isBlank()) {
            throw new IllegalArgumentException("Contact ID must not be null or blank.");
        }
        return contactId.trim();
    }

    private Contact requireContact(String id) {
        Contact contact = primaryIndex.get(id);
        if (contact == null) {
            throw new ContactNotFoundException(id);
        }
        return contact;
    }
}
