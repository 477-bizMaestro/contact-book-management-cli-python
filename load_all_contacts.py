def load_all_contacts():
    all_contacts = []
    try:
        with open("Contact_Book.csv", "r") as bookFile:
            for line in bookFile:
                fields = line.strip().split(", ")
                if len(fields) == 5:
                    serial, name, email, phone_no, address = fields
                    contact = {
                        "serial": int(serial),
                        "name": name,
                        "email": email,
                        "phone_no": int(phone_no),
                        "address": address
                    }
                    all_contacts.append(contact)
    except FileNotFoundError:
        print("No previous contact data found. Starting with an empty list.")
    return all_contacts


