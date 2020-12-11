# Rock Paper Scissor Game :
import random

print("Hey! Let's play Rock Paper Scissor Game!")

while True:
    print()
    print('====================')
    print()
    print()
    print("You have three option :")
    print("[ 1 ] Rock \n[ 2 ] Paper \n[ 3 ] Scissor")
    print()

    total_choice = ["rock", "paper", "scissor"]
    comp_choice = random.choice(total_choice)
    choice = input("choose 1, 2, 3 : ")

    print()
    print("--------------------------")

    if choice == '1':
        selection = "rock"
        print("You choose Rock!")
    elif choice == '2':
        selection = "paper"
        print("You choose Paper!")
    elif choice == '3':
        selection = "scissor"
        print("You choose Scissor!")
    else:
        print("Wrong Input")
        exit()

    print(f"Computer Choose {comp_choice}!")
    print("--------------------------")
    print()

    # Decide Who wins and declare winner
    if selection == 'rock' and comp_choice == 'paper' or selection == 'paper' and comp_choice == 'scissor' or selection == "scissor" and comp_choice == 'rock':
        print("YOU LOSE!!!!")
    elif selection == 'rock' and comp_choice == 'scissor' or selection == 'paper' and comp_choice == 'rock' or selection == 'scissor' and comp_choice == 'paper':
        print("YOU WINS!!!!")
    else:
        print("It's a draw!")
