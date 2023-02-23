import random
choices = ['Rock','Paper','Scissors']
Comp_score = 0
Your_score = 0
No_of_rounds = 0

while No_of_rounds < 3:
    Comp_choice = random.choice(choices)
    Your_choice = input("Pick your choice; ")
    No_of_rounds += 1
    if Comp_choice == Your_choice:
        print("It is a tie")
    elif (Comp_choice == 'Rock' and Your_choice == 'Scissors') or (Comp_choice == 'Paper' and Your_choice == 'Rock') or (Comp_choice == 'Scissors' and Your_choice == 'Paper'):
        print ("You lose this round")
        Comp_score += 1
    elif (Your_choice == 'Rock' and Comp_choice == 'Scissors') or (Your_choice == 'Paper' and Comp_choice == 'Rock') or (Your_choice == 'Scissors' and Comp_choice == 'Paper'):
        print("You win this round")
        Your_score += 1
    else:
        print("Invalid option")
    if (Comp_score == 2) or (Your_score == 2):
        break
    if No_of_rounds =='3':
        break
    print('Round:',No_of_rounds)

if Your_score > Comp_score:
    print("You win")
else:
    print("You lose. Try next time")


