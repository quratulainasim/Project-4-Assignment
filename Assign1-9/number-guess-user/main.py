import random
def main():
    user_input=int(input("Enter a number between 1-10: "))
    random_num=random.randint(1, 10)
    while True:
        if user_input == random_num:
            print("Congratulations! your number is right.")
            break
        elif user_input == 0:
            print("Exiting the game")
            break
        else:
             print("Enter again number")
             user_input=int(input("Enter a new number:"))
if __name__ == '__main__':             
    main()

