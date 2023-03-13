import random

winning_pos = 100
winner = None
ladders = {1:38,4:14,9:31,21:43,28:84,51:67,72:91,80:99}
snakes = {17:7,54:34,62:19,64:60,87:36,93:73,95:75,98:79}
players = []

def welcome_msg():
    message = """
    Welcome to Snake and Ladder Game.
    Version: here n now!!!

    Rules:
    1. Initially all the players are at starting position i.e. 0. 
        Take it in turns to roll the dice. 
        Move forward the number of spaces shown on the dice.
    2. If you land at the bottom of a ladder, you can move up to the top of the ladder.
    3. If you land on the head of a snake, you must slide down to the bottom of the snake.
    4. The first player to get to the FINAL position is the winner.
    5. Hit enter to roll the dice.
    6. Sign up the number of players and names to begin
    """
    print(message)

def player_names():
    choose = int(input("How any players are you? "))
    try:
        value = int(choose)
    except ValueError:
        print("Please, type a valid integer number!")
    if choose > 5:
        print("max of 4 players allowed")
    if choose == 1:
        print("More than one player required")
    if choose == 4:
        player_1 = None
        while not player_1:
            player_1 = input("Enter Player 1 name: ")
            players.append(player_1)
        player_2 = None
        while not player_2:
            player_2 = input("Enter Player 2 name: ")
            players.append(player_2)
        player_3 = None
        while not player_3:
            player_3 = input("Enter Player 3 name: ")
            players.append(player_3)
        player_4 = None
        while not player_4:
            player_4 = input("Enter Player 4 name: ")
            players.append(player_4)
        
        return (player_1,player_2,player_3,player_4)

    elif choose == 3:
        player_1 = None
        while not player_1:
            player_1 = input("Enter Player 1 name: ")
            players.append(player_1)
        player_2 = None
        while not player_2:
            player_2 = input("Enter Player 2 name: ")
            players.append(player_2)
        player_3 = None
        while not player_3:
            player_3 = input("Enter Player 3 name: ")
            players.append(player_3)
        return player_1,player_2,player_3
        
    elif choose == 2:
        player_1 = None
        while not player_1:
            player_1 = input("Enter Player 1 name: ")
            players.append(player_1)
        player_2 = None
        while not player_2:
            player_2 = input("Enter Player 2 name: ")
            players.append(player_2)
        return player_1,player_2


def dice_roll():
    dice_value = random.randint(1,6)
    print("You've picked: " + str(dice_value))
    return dice_value


def get_pos(player_name,current_pos,dice_value):
    initial_pos = current_pos
    current_pos = current_pos + dice_value

    if current_pos >= winning_pos:
        winner = player_name
        final_pos = winning_pos #to avoid getting past 100
        print("game over")
        print(winner + " wins the game !!!")
        

    elif current_pos in snakes:
        final_pos = snakes.get(current_pos)
        print("Snake bite!!!. You've moved from " + str(current_pos) + " to " +  str(final_pos))

    elif current_pos in ladders:
        final_pos = ladders.get(current_pos)
        print("Ladder Boost!!!. You've moved from " + str(current_pos) + " to " + str(final_pos))

    else:
        final_pos = current_pos

    return final_pos

def play_game():
    welcome_msg()
    player_names()
    player_starting_pos = 0
    while player_starting_pos < 100:

        for player in players:
            input_ = input(player + " Hit enter to roll dice: ")
            print("Rolling dice: ")
            dice_value = dice_roll()
            print(player + " moving...")
            player_starting_pos = get_pos(player,player_starting_pos,dice_value)
            print(player,player_starting_pos)
        if player_starting_pos >= 100:
            break
           

