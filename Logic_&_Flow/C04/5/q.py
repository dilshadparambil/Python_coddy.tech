def display_menu():
    print("Contact Book Menu:\n1. Add Contact\n2. View Contact\n3. Edit Contact\n4. Delete Contact\n5. List All Contacts\n6. Exit")

def add_contact(contact_book):
    name=input()
    phone=input()
    email=input()
    address=input()
    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")

def view_contact(contact_book):
    contact_name=input()
    if contact_name in contact_book:
        print(f"Name: {contact_name}\nPhone: {contact_book[contact_name]['phone']}\nEmail: {contact_book[contact_name]['email']}\nAddress: {contact_book[contact_name]['address']}")
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    contact_name=input()
    if contact_name in contact_book:
        phone=input()
        email=input()
        address=input()
        if phone!='' and email!='' and address!='':
            contact_book[contact_name] = {
            "phone": phone,
            "email": email,
            "address": address
            }   
        print("Contact updated successfully!")
    else:
        print("Contact not found!")


