import random
def main():

    secret_number = random.randint(1, 99)

    guess_num = int(input("Enter a number: "))

    while guess_num != secret_number:

        if guess_num < secret_number:
         print("Enter number is too low")
        else:
           print("Enter number is too high")
        print() 
        guess_num = int(input("Enter a new guess: "))  
        
    print("Congrats! The number was: " + str(secret_number))
        
if __name__ == '__main__':
  main()      