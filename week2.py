import random
words = ['foxglove','luxury','subway','rudeboy','haystack']
word_choice = random.choice(words)
import string

def hangman():
    word_choice_letters = set(word_choice) #whats already been guessed and is in the word
    picked_letters = set() #storing every user input letter
    alphabet = set(string.ascii_uppercase)
    lives = 6
    while len(word_choice_letters) > 0 and lives > 0:
        print('You have picked: ',''.join(picked_letters))
        word_list = [letter if letter in picked_letters else '-' for letter in word_choice]
        print('Current words: ',''.join(word_list))

        player_choice = input("Guess a letter: ").upper()
        try:
            player_choice = str(player_choice) # input is a string
            player_choice = '' # input is one character
            if player_choice in alphabet - picked_letters: # avoids picking a letter twice
                picked_letters.add(player_choice)
            else:
                print("You've already entered this character, Enter a new character")
                if player_choice in word_choice_letters:
                    word_choice_letters.remove(player_choice)
                else:
                    print("Sorry, the letter is not part of the word")
                    lives = lives - 1         

        except:
            player_choice = int(player_choice)
            print("Invalid input. Pick an alphabet")
            player_choice != ''
            print ("Please input one character at a time")

        if lives == 0:
            print('Game lost')
        else:
            print('You win',word_choice)

hangman()
