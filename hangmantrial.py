words = ['foxglove','luxury','subway','rudeboy','haystack']
import random

def hangman():
    comp_choice = random.choice(words)
    chosen_letters = []
    lives = 6
    word_progress = "-" * len(comp_choice)

    while lives > 0 and word_progress != comp_choice:
        player_choice = input("Enter your guess: ")
        if len(player_choice) == 1:
            if player_choice in comp_choice:
                print("Correct guess: ",player_choice, "is in the word")
                chosen_letters.append(player_choice)
                word_as_list = list(word_progress)
                indices = [i for i,letter in enumerate(comp_choice) if letter == player_choice]
                for index in indices:
                    word_as_list[index] = player_choice
                word_progress = "".join(word_as_list)
                print(word_progress)
                if "-" not in word_progress:
                    break
                else:
                    continue
            elif player_choice in chosen_letters:
                print("you have already picked this letter")
            else: #player choice is not in the word and also not picked
                print("Letter is not in the word")
                chosen_letter.append(player_choice)
                lives -= 1

        else:
            print("Invalid character. Please pick one character")
        print(word_progress)
    if word_progress in comp_choice:
        print("Correct. The word is ",comp_choice)
    else:
        print("Sorry, you lost")
hangman()