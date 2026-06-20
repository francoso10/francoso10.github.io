package contactservice;

import java.util.HashMap;
import java.util.Map;

public class ContactService {
    private final Map<String, Contact> contacts = new HashMap<>();

    // Adds a new contact if the ID is unique
    public void addContact(Contact contact) {
        if (contacts.containsKey(contact.getContactId())) {
            throw new IllegalArgumentException("Contact ID already exists");
        }
        contacts.put(contact.getContactId(), contact);
    }

    // Deletes a contact by ID
    public void deleteContact(String contactId) {
        if (!contacts.containsKey(contactId)) {
            throw new IllegalArgumentException("Contact ID not found");
        }
        contacts.remove(contactId);
    }

    // Updates a contact's first name
    public void updateFirstName(String contactId, String firstName) {
        getContact(contactId).setFirstName(firstName);
    }

    // Updates a contact's last name
    public void updateLastName(String contactId, String lastName) {
        getContact(contactId).setLastName(lastName);
    }

    // Updates a contact's phone number
    public void updatePhone(String contactId, String phone) {
        getContact(contactId).setPhone(phone);
    }

    // Updates a contact's address
    public void updateAddress(String contactId, String address) {
        getContact(contactId).setAddress(address);
    }

    // Retrieves a contact by ID
    public Contact getContact(String contactId) {
        if (!contacts.containsKey(contactId)) {
            throw new IllegalArgumentException("Contact not found");
        }
        return contacts.get(contactId);
    }
}
