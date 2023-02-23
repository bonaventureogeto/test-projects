phone_dict = {}

add_contact = True

while add_contact:
    Contact_name = input("Enter the contact name: ")
    Phone_number = int(input("Enter the phone number: ")
    if Contact_name in phone_dict:
        print("Contact already exists")
    else:
        phone_dict[Contact_name] = Phone_number

    add_contact = False

print(phone_dict.items())

delete_contact = True

while delete_contact:
    Contact_name = input("Enter the contact name: ")
    if Contact_name in phone_dict:
        del phone_dict[Contact_name]
    else:
        print("Contact doesn't exist)

    delete_contact = False

Contact_search = True

while Contact_search:
    Contact_name = input("Enter a contact name: ")
    if phone_dict.get(Contact_name) == None:
        print("Contact does not exist")
    else:
        print(value)

Print_all_contacts = True
Options = ["yes","no"]
while Print_all_contacts:
    view_all = input("View all contacts, ")
    if view_all == "yes":
        print(phone_dict.items())
    else:
        break

