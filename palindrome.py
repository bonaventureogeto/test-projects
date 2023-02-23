def palindrome_checker (text):
    with open('dictionary.txt', 'r') as file:
        text = file.read()

    for word in text:
        word_inv = word[::-1]
        if word_inv == word:
            print(word, "Is a palindrome")
        else:
            print(word, "Is not a palindrome")


palindrome_checker("word")



