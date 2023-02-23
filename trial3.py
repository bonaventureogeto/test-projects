fhand = open('dictionary.txt')
for line in fhand:
    line_inv = line[::-1]
    if line == line_inv:
        print(line, "Is a palindrome")
   