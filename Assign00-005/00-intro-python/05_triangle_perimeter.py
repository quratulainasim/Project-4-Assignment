def length():
    side_a=float(input("Enter the length of side a: "))
    side_b=float(input("Enter the length of side b: "))      
    side_c=float(input("Enter the length of side c: "))
    
    print("The perimeter of the triangle is : " + str(side_a + side_b + side_c))
if __name__ == "__main__":
    length()    