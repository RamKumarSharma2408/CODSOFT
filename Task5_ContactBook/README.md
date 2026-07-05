# Task 5 – Contact Book

## CODSOFT Python Programming Internship

### Overview
A command-line contact management application. Users can store, view, search, update, and delete contacts, each containing a name, phone number, email, and address. All data is saved to a JSON file so contacts persist between sessions.

### Features
- **Add Contact** – Save a new contact with name, phone, email, and address.
- **View Contact List** – Display all saved contacts with names and phone numbers.
- **Search Contact** – Find contacts by name or phone number (partial matches supported).
- **Update Contact** – Edit any field of an existing contact.
- **Delete Contact** – Remove a contact from the list.
- **Persistent Storage** – Contacts are saved to `contacts.json`.

### How to Run
```bash
python3 task5_contact_book.py
```

### Sample Usage
```
===== CONTACT BOOK =====
1. Add Contact
2. View All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Choose an option (1-6): 1

Enter contact details:
Name: John Doe
Phone Number: 9876543210
Email: john@example.com
Address: 123 Main St
Contact 'John Doe' added successfully!
```

### Tech Used
- Python 3 (`json` module from the standard library for persistent storage)

### Possible Improvements
- Add duplicate contact detection
- Export/import contacts as CSV
- Build a GUI version using Tkinter

---
*Part of the CODSOFT Python Programming Internship – [www.codsoft.in](https://www.codsoft.in)*
