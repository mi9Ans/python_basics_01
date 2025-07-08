# Mini Contact Book 📖

contacts = {
    "Ravi": "9876543210",
    "Neha": "8765432109"
}

while True:
    print("\n--- Contact Book Menu ---")
    print("1. View All Contacts")
    print("2. Search Contact")
    print("3. Add / Update Contact")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        for name, number in contacts.items():
            print(name, "➡️", number)

    elif choice == "2":
        name = input("Enter contact name to search: ")
        print("Number:", contacts.get(name, "Not Found"))

    elif choice == "3":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        contacts[name] = number
        print("Contact saved.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
