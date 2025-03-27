import math

def theorum():
    side_ab:float= float(input("Enter side AB : "))
    side_bc:float= float(input("Enter side BC : "))    
    side_ac:float= math.sqrt(side_ab**2 + side_bc**2)
    print("The length of AC is: " + str(side_ac))
if __name__ == "__main__":
    theorum()