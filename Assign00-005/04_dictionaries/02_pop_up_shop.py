def main():
    all_fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}

    fruits_cost = 0
    for fruits in all_fruits:
        price = all_fruits[fruits]
        amount = int(input("How many (" + fruits +") do you buy?: "))
        fruits_cost+= (price * amount)
    print("your total amount  $ " + str(fruits_cost))    

if __name__ == '__main__':
    main() 