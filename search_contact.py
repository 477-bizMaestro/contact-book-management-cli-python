def search_contact(all_contacts):
    if not all_contacts:
        print("No contacts available to search.")
        return

    phone_no_to_search = input("Enter the phone number to search: ").strip()

    found_contacts = [
        contact for contact in all_contacts if str(contact["phone_no"]) == phone_no_to_search
    ]

    if found_contacts:
        print("Search Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']} | E-mail: {contact['email']} | Phone Number: {contact['phone_no']} | Address: {contact['address']}")
    else:
        print("No contact found with the given phone number.")

