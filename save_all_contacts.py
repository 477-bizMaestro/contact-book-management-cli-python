def save_all_contacts(all_contacts):
    with open("Contact_Book.csv", "w") as bookFile:
        for contact in all_contacts:
            line = f"{contact['serial']} , {contact['name']} , {contact['email']} , {contact['phone_no']} , {contact['address']}\n"
            bookFile.write(line)