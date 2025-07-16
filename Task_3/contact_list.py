contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[phone] = {"name": name, "email": email, "address": address}
    print("✅ Contact added successfully!")

def view_contacts():
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n--- Contact List ---")
    for phone, info in contacts.items():
        print(f"Name: {info['name']} | Phone: {phone}")

def search_contact():
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    for phone, info in contacts.items():
        if keyword in info['name'].lower() or keyword in phone:
            print("\n--- Contact Found ---")
            print(f"Name: {info['name']}")
            print(f"Phone: {phone}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            found = True
    if not found:
        print("❌ Contact not found.")

def update_contact():
    phone = input("Enter phone number of contact to update: ")
    if phone in contacts:
        print("Enter new details (leave blank to keep existing):")
        name = input(f"New name ({contacts[phone]['name']}): ") or contacts[phone]['name']
        email = input(f"New email ({contacts[phone]['email']}): ") or contacts[phone]['email']
        address = input(f"New address ({contacts[phone]['address']}): ") or contacts[phone]['address']
        contacts[phone] = {"name": name, "email": email, "address": address}
        print("✅ Contact updated.")
    else:
        print("❌ Contact not found.")

def delete_contact():
    phone = input("Enter phone number of contact to delete: ")
    if phone in contacts:
        confirm = input("Are you sure? (y/n): ").lower()
        if confirm == 'y':
            del contacts[phone]
            print("🗑️ Contact deleted.")
    else:
        print("❌ Contact not found.")

def main():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("❗ Invalid option. Please try again.")

main()






