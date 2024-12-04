from save_all_contacts import save_all_contacts

def add_contact(all_contacts):
    serial = len(all_contacts) + 1
    name = input("Contact Name: ")
    email = input("Contact Email: ")
    phone_no = int(input("Contact Phone Number: "))

    for contact in all_contacts:
        if contact['phone_no'] == phone_no:
            print(f"Error, the phone number {phone_no} already exists in {name}")
            return all_contacts


    address = input("Contact Address: ")

    contact = {
        "serial" : serial,
        "name" : name,
        "email" : email,
        "phone_no" : phone_no,
        "address" : address
    }


    all_contacts.append(contact)
    save_all_contacts(all_contacts)

    print("Contact added successfully.")

    return all_contacts


