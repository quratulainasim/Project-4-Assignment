import random

option=["rock","paper","scissors"]

computer_input=random.choice(option)

while True:
    user_input=input("Enter your option or quit to exit: ").lower()
    if user_input =="quit":
        print("Exit")
        break
    if user_input == computer_input:
        print("Game is tie!")
    elif user_input == "rock" and computer_input == "paper":
        print("You Win")
    elif user_input == "paper" and computer_input == "scissors":
        print("You Win")
    elif user_input == "scissors" and computer_input == "rock":
        print("You Win")
     
    else:
        print("Computer Win!")