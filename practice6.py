"""

Phone Book Application: Develop a simple phone book application that allows users to add
contacts, remove contacts, and display the list of contacts. Use a dictionary to store contact
names and phone numbers, and implement for loops to iterate over the dictionary for various
operations.

"""
phone_book = {}

def display_menu():

    print("\nPhone Book Menu:")
    print("1. Add contacts")
    print("2. Remove contacts")
    print("Display the list of conctacts")
    print("Exit")

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    if name in phone_number:
        print(f"Contact '{name} already exist. ")
    phone_book[name] = phone_number
    print(f"Contact '{name} added/updated succesfully.")


def remove_contacts():
    name = input("Enter contact name to remove: ")
    if name in phone_book[name]:
        del phone_book[name]
        print(f"Contact {name} removed succesfully.")
    else:
        print(f"Contact {name} not found.")


def display_contacts():
    if not phone_book:
        print("No contacts found.")
    else:
        print(f"/nConctact List:")
        for name, phone_number in phone_book.items():
            print(f"Name: {name}, Phone Number: {phone_number}")

while True:
    display_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        remove_contacts()
    elif choice == "3":
        display_contacts()
    elif choice == "4":
        print("Exiting Phone Book. Goodbye.")
        break
    else:
        print("Invalid choice. Please try again.")        