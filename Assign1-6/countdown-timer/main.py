import time

def main():
    number=int(input("Enter a number: "))
    while number > 0:
        print(number)
        time.sleep(1)
        number -= 1
    print("\nCOMPLETED!")

if __name__ == '__main__':
    main()        