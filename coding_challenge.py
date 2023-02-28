import re

def extract_phone_numbers(string):
    pattern = re.compile("(?\d{3})?[-\s]?\d{3}[-.\s]?\d{4}")
    result = pattern.findall(string)
    print(result)



def extract_email_addresses(string):
    pattern = re.compile("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[a-zA-Z]{2,}")
    result = pattern.findall(string)
    print(result)



def replace_email_addresses(string, replacement):
    pattern = re.commpile("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[a-zA-Z]{2,}")
    result = pattern.sub('string','replacement')
    print(result)



extract_phone_numbers(string)
extract_email_addresses(string)
replace_email_addresses(string,replacement)