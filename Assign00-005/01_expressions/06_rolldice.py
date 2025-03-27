import random
def roll_dice():
    die_1:int = random.randint(1,6)
    die_2:int = random.randint(1,6)
    total:int = die_1 + die_2
    print("Dice have 6 sides each")
    print(f"Die 1 :{die_1}")
    print(f"Die 2 :{die_2}")
    print("Total of two dice:", total)
if __name__ == "__main__":
    roll_dice()