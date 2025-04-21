import random

def main():
    random_num = random.randint(1, 10)
    
    print("Guess the number between 1 and 10 (enter 0 to exit):")

    while True:
        try:
            user_input = int(input("Enter your guess: "))
            
            if user_input == 0:
                print("Exiting the game.")
                break
            elif user_input == random_num:
                print("Congratulations! Your number is right.")
                break
            else:
                print("Wrong guess, try again.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == '__main__':
    main()

