import random

def roll_dice():
    die_1:int = random.randint(1,6)
    die_2:int = random.randint(1,6)
    total:int = die_1 + die_2
    print("Total of two dice:", total)

def main():
    die_1 = 6
    print (f" die_1 in main is {die_1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print (f" die_1 in main is {die_1}")
if __name__ == "__main__":
    main()