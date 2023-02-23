phone_dict={}

new_contacts ={"Vic":1234,
"Jane":2345,
"John":3456,
"Alice":4567,
"Peter":5678,
"Liz":6789}

phone_dict.update(new_contacts)

def add_contact(name,value):
    global phone_dict
    name = input("Enter the contact name: ")
    if phone_dict.has_key(name):
        print("Sorry, contact already exixts")
    else:
        value = int(input("Enter Phone Number, "))
    phone_dict[name] = value

add_contact("name","value")

print(phone_dict.items())