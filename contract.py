import json
import os
FILE = "contacts.json"
def load_contacts():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as file:
                data = json.load(file)
            if isinstance(data, dict):
                return data
            print("Invalid contacts file format.")
        except (json.JSONDecodeError, OSError):
            print("Error loading contacts.")
    return {}
def save_contacts(contacts):
    try:
        with open(FILE, "w") as file:
            json.dump(contacts, file, indent=4)
        return True
    except OSError:
        print("Error saving contacts.")
        return False
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    if not name or not phone:
        print("Name and phone cannot be empty!")
        return
    if not phone.isdigit() or len(phone) != 10:
        print("Enter a valid 10-digit phone number!")
        return
    contacts[name] = phone
    if save_contacts(contacts):
        print("Contact added successfully!")
def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print("Phone number:", contacts[name])
    else:
        print("Contact not found!")
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        if save_contacts(contacts):
            print("Contact deleted successfully!")
    else:
        print("Contact not found!")
def view_contacts(contacts):
    if not contacts:
        print("No contacts available!")
    else:
        for name, phone in contacts.items():
            print(name, ":", phone)
def main():
    contacts = load_contacts()
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View Contacts")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_contact(contacts)
            elif choice == 2:
                search_contact(contacts)
            elif choice == 3:
                delete_contact(contacts)
            elif choice == 4:
                view_contacts(contacts)
            elif choice == 5:
                print("Thank you!")
                break
            else:
                print("Please choose between 1 and 5.")
        except ValueError:
            print("Invalid input! Enter a number.")


main()
