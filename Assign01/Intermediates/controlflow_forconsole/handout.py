import random

Round=5
def main():

    score=0

    for i in range(Round):
        print("Round",i+1)
        my_num = random.randint(1, 100)
        comp_num = random.randint(1, 100)
        print("My number is", my_num)

        print("Computer's number is", comp_num)

        choice:str=input("Do you want to guess my number higher or lower number to computer number? ")
        higher_number:bool=choice=="higher" and my_num>comp_num
        lower_number:bool=choice=="lower" and my_num<comp_num
        if higher_number or lower_number:
            print("You number is right!" )
            score+=1

        else:
            print("You lose!")
       
        print("Your total score is : ", score)
if __name__ == "__main__":
    main()        