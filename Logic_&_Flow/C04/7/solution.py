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

def delete_contact(contact_book):
    contact_name=input()
    if contact_name in contact_book:
        del contact_book[contact_name]  
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else :
        for key in contact_book:
            print(f"Name: {key}\nPhone: {contact_book[key]['phone']}\nEmail: {contact_book[key]['email']}\nAddress: {contact_book[key]['address']}\n")

contact_book={}
program=True
while program:
    display_menu()
    choice=int(input())
    if choice==1:
        add_contact(contact_book)
    elif choice==2:
        view_contact(contact_book)
    elif choice==3:
        edit_contact(contact_book)
    elif choice==4:
        delete_contact(contact_book)
    elif choice==5:
        list_all_contacts(contact_book)
    elif choice==6:
        program=False
