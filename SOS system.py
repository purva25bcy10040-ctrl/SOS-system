import random

contacts = {}  # Store trusted contacts as {name: phone/email}

def add_contact():
    name = input("Contact name: ")
    info = input("Phone/Email: ")
    contacts[name] = info
    print(f"Added {name}.")

def view_contacts():
    if not contacts:
        print("No contacts saved.")
    else:
        for name, info in contacts.items():
            print(f"{name}: {info}")

def send_sos():
    if not contacts:
        print("Add contacts first!")
        return
    location = input("Enter your location or GPS coords: ")
    message = input("Enter SOS message: ")
    print("\nSending alert to contacts...")
    for name, info in contacts.items():
        print(f"Alert sent to {name} at {info}")
        print(f"Message: {message}\nLocation: {location}")
    print("All alerts sent.\n")

def main():
    while True:
        print("1. Add Contact\n2. View Contacts\n3. Send SOS\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            send_sos()
        elif choice == "4":
            print("Stay safe!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
