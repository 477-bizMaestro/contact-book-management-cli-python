import add_contact
import view_all_contacts
import delete_contact
import search_contact
from load_all_contacts import load_all_contacts

all_contacts = load_all_contacts()

while True:
    print("\nWelcome to Contact Book Management System")
    print("Operation Menu: ")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit the System")

    option = input("Select an option from the operation menu: ")

    if option == "1":
        all_contacts = add_contact.add_contact(all_contacts)
    
    elif option == "2":
        print("\nContacts: ")
        view_all_contacts.view_all_contacts(all_contacts)

    elif option == "3":
        search_contact.search_contact(all_contacts)

    elif option == "4":
        all_contacts = delete_contact.delete_contact(all_contacts)
        
    elif option == "5":
        print("System exited successfully!")
        break
    else:
        print("Sorry, your input is invalid!! Please try to select from the menu.")