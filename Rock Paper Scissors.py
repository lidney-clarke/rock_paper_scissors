from random import randint

# variables
# choices - list of strings that represents choices
# rnd - random integer as pointer to selection from choices
# computer - string result of computer choice
# player - string input from player


#create a list of play options
choices = ["Rock", "Paper", "Scissors"]

#assign a random choice to the computer, use list
rnd = randint(0,2)
computer = choices[rnd]

#Initialize player choice
player = ""

while player != "Quit":
    player = input("Rock, Paper, Scissors?")
    print("Computer chose:"+computer+".")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #pick a new choice
    #assign a random choice to the computer, use list
    rnd = randint(0,2)
    computer = choices[rnd]
