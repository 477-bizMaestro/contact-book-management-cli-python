def view_all_contacts(all_contacts):
    if all_contacts != []:
        for contact in all_contacts:
            print(f"Contact No. {contact['serial']} | Name: {contact['name']} | E-mail: {contact['email']} | Phone Number: {contact['phone_no']} | Address: {contact['address']}")

    else:
        print("Sorry, your desired contact is not in the book!")