"""
CODSOFT Python Programming Internship
Task 5 - Contact Book

A command-line contact book that lets the user:
- Add a contact (name, phone, email, address)
- View all contacts
- Search for a contact by name or phone number
- Update an existing contact
- Delete a contact

Contacts are stored in a JSON file so they persist between runs.
"""

import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def add_contact(contacts):
    print("\nEnter contact details:")
    name = input("Name: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    if not name or not phone:
        print("Name and phone number are required.")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
    })
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts saved yet.")
        return
    print("\nAll Contacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")


def find_matches(contacts, query):
    query = query.lower()
    return [
        c for c in contacts
        if query in c["name"].lower() or query in c["phone"]
    ]


def display_contact_details(contact):
    print(f"Name:    {contact['name']}")
    print(f"Phone:   {contact['phone']}")
    print(f"Email:   {contact['email']}")
    print(f"Address: {contact['address']}")


def search_contact(contacts):
    query = input("\nEnter name or phone number to search: ").strip()
    matches = find_matches(contacts, query)

    if not matches:
        print("No matching contacts found.")
        return

    print(f"\nFound {len(matches)} match(es):")
    for i, contact in enumerate(matches, start=1):
        print(f"\n{i}.")
        display_contact_details(contact)


def update_contact(contacts):
    query = input("\nEnter name or phone number of the contact to update: ").strip()
    matches = find_matches(contacts, query)

    if not matches:
        print("No matching contacts found.")
        return

    if len(matches) > 1:
        print(f"\nFound {len(matches)} matches:")
        for i, contact in enumerate(matches, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        try:
            index = int(input("Select the number of the contact to update: ")) - 1
            if not (0 <= index < len(matches)):
                print("Invalid selection.")
                return
            contact = matches[index]
        except ValueError:
            print("Please enter a valid number.")
            return
    else:
        contact = matches[0]

    print("\nLeave a field blank to keep it unchanged.")
    new_name = input(f"Name [{contact['name']}]: ").strip()
    new_phone = input(f"Phone [{contact['phone']}]: ").strip()
    new_email = input(f"Email [{contact['email']}]: ").strip()
    new_address = input(f"Address [{contact['address']}]: ").strip()

    if new_name:
        contact["name"] = new_name
    if new_phone:
        contact["phone"] = new_phone
    if new_email:
        contact["email"] = new_email
    if new_address:
        contact["address"] = new_address

    save_contacts(contacts)
    print("Contact updated successfully!")


def delete_contact(contacts):
    query = input("\nEnter name or phone number of the contact to delete: ").strip()
    matches = find_matches(contacts, query)

    if not matches:
        print("No matching contacts found.")
        return

    if len(matches) > 1:
        print(f"\nFound {len(matches)} matches:")
        for i, contact in enumerate(matches, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        try:
            index = int(input("Select the number of the contact to delete: ")) - 1
            if not (0 <= index < len(matches)):
                print("Invalid selection.")
                return
            contact = matches[index]
        except ValueError:
            print("Please enter a valid number.")
            return
    else:
        contact = matches[0]

    contacts.remove(contact)
    save_contacts(contacts)
    print(f"Contact '{contact['name']}' deleted successfully!")


def main():
    contacts = load_contacts()

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
