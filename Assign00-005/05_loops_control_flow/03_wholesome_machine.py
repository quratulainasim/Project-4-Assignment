AFFIRMATION = "I will do every thing which would be in my mind."

def main():
    print("Please type the following affirmation:" + (AFFIRMATION))
    user_output = input()
    while user_output != AFFIRMATION:

      print("That was not the affirmation.")

      print("Please type the following affirmation:" + (AFFIRMATION))
      user_output = input()
    print("Thats right!") 

if __name__ == '__main__':
    main()       