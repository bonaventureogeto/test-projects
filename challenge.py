#step 1
f = open('name.csv','r')
books = f.read()
books = {"Title":" ",
"Author": " ",
"ISBN": " ",
"Price": " "
}

#step 2
f = books.get("Author")
print(f)




#step 3
g = books.get("ISBN")
print(g)




#step 4
h = books.get("Max Price","Min Price")
print(h)
    