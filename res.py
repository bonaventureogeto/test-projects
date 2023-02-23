phone_dict={}

new_contacts ={"Vic":1234,
"Jane":2345,
"John":3456,
"Alice":4567,
"Peter":5678,
"Liz":6789}

phone_dict.update(new_contacts)
print(phone_dict.items())

if "Jane" in phone_dict:
    print("Yes")
add_contact = True

while add_contact:
    Contact_name = input("Enter the contact name: ")
    Phone_number = int(input("Enter the phone number: ")
    if phone_dict.get(Contact_name) == ("None"):
        phone_dict[Contact_name] = Phone_number
    else:
        print("Contact already exists")

    add_contact = False