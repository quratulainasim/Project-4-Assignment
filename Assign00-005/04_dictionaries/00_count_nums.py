def main():
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        number = int(user_input)
        user_numbers.append(number)
    
    counts = {}
    for number in user_numbers:
        if number not in counts:
            counts[number] = 1
        else:
            counts[number] += 1
    
    for number, count in counts.items():
        print(number, "occurs", count, "times", ",", end="")

if __name__ == "__main__":
    main()
  

