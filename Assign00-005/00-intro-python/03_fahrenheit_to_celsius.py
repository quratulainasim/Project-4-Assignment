def main():
    user_degree=float(input("Enter temperature in Farenheit : "))
    celsius=(user_degree -32)*5/9
    print(f"Temperature : {user_degree}F= {celsius}C")
          
if __name__ == '__main__':
    main()
