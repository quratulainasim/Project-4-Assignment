def leap_year():
    user_year:int = int(input("Enter a year: "))
    if user_year % 4 ==0:
        print(f"{user_year} is a leap year.")
    else:
        print(f"{user_year} is not a leap year.")
    if user_year % 100 ==0:
        print(f"{user_year} is not a leap year.")
    else:
        print(f"{user_year} is a leap year.")
    if user_year % 400 ==0:
        print(f"{user_year} is a leap year.")       
    else:
        print(f"{user_year} is not a leap year.")
if __name__ == '__main__':  
    leap_year()    
        