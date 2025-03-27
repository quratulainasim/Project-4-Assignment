def conversion():
    user_feet=float(input("Enter number of feet : "))
    inches_in_feet: int = 12
    converted_inches : int =user_feet *inches_in_feet
    print(f"{user_feet} feet is equal to {converted_inches} inches")
if __name__ == "__main__":
    conversion()