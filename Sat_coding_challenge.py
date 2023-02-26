def parse_file(file_path):
    fhand = open(file_path,'r')
    file_contents = fhand.read()

    file_contents = file_contents.rstrip()
    
    for string in file_contents:
        lists = string.split(',')
    
address_book={}
def add_dict(name,value):
    for list in lists:
        name = list[0]
        value = list[1]

add_dict('', '')
address_book.update(add_dict)
        

parse_file('address_book.txt')

print(address_book)

