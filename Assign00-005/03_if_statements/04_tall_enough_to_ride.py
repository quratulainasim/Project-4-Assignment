MINIMUM_HEIGHT = 50
def main():
    while True:
        user_height = input("Enter your height in inches: ")

        if user_height == "":
            break

        try:
            user_height = float(user_height)

            if user_height >= MINIMUM_HEIGHT:
                print("You are tall enough to ride.")
            else:
                print("You are not tall enough to ride.")

        except ValueError:
            print("Please enter height.")
        
if __name__ == '__main__':
    main()