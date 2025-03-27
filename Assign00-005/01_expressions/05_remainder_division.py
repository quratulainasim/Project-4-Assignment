def division():
    first_num:int = int(input("Enter the first number to be divided :"))
    second_num:int = int(input("Enter the second number to divide by :"))
    remainder:int = first_num % second_num
    print(f"The reminder of {first_num} divided by {second_num} is {remainder}")
if __name__ == "__main__":
    division()