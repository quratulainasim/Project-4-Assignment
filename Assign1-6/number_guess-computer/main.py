import random

user_input=int(input("Enter the number between 1-10: "))
computer_input= random.randint(1, 10)
print(f"Computer guess the number :{computer_input}")

while True:
    feedback =input("Computer guess number is Low ,High ,Right: ")
    if feedback == "Right":
        print("Congratulation! YOU WON THE GAME")
        break
    elif feedback == "Low":
        print("Enter number is too Low") 
    elif feedback == "High":
        print("Enter number is too High")
    else:
        print("Wrong Input!")
        continue
    computer_input= random.randint(1, 10)
    print(f"Computer guess the new number :{computer_input}")