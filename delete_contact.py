from save_all_contacts import save_all_contacts

def delete_contact(all_contacts):
    if not all_contacts:
        print("No contacts available to delete.")
        return all_contacts

    phone_no_to_delete = input("Enter the phone number of the contact to delete: ")
    for contact in all_contacts:
        if str(contact["phone_no"]) == phone_no_to_delete:
            all_contacts.remove(contact)
            save_all_contacts(all_contacts)
            print("Contact deleted successfully!")
            return all_contacts

    print("Contact not found.")
    return all_contacts
