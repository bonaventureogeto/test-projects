phone_dict={}

new_contacts ={"Vic":1234,
"Jane":2345,
"John":3456,
"Alice":4567,
"Peter":5678,
"Liz":6789}

phone_dict.update(new_contacts)
print(phone_dict.items())

if "Vic" in phone_dict:
    print("Yap")


#if phone_dict.get("Vic") == None:
    #print("Not Present")
#else:
    #print("The value is, ")

#print(phone_dict.get("Vic"))

#def cont_check(dic,key):
    #key = input("Enter the contact name: ")
    #if dic.has_key(key):
        #print('Present, value = ',dic[key])
    #else:
        #print('Not present')

#cont_check(phone_dict,"key")


#def add_contact(inp,value):
    #inp = input("Enter the contact name: ")
    #if phone_dict.has_key(inp):
        #print("Sorry, contact already exixts")
    #else:
        #value = input("Enter Phone Number, ")
        #phone_dict["inp"] = "value"

#add_contact("inp","value")
