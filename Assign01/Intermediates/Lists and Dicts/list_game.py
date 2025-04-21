fruits_list=["orange","apricot","peach","watermelon","strawberry"]
def fruits_access(fruits_list,index):
    if 0 <= index < len(fruits_list):
        return f"Element at index {index} is {fruits_list[index]}"
    return "Index out of range"

def modify_fruits(fruits_list,index,new_value):
    if 0 <= index < len(fruits_list):
        fruits_list[index] = new_value
        return f"Element at index {index} is modified to {new_value}"
    return "Index out of range"
def slicing_fruits(fruits_list,start_index,end_index):
    if 0 <= start_index < len(fruits_list) and 0 <= end_index < len(fruits_list):
        return fruits_list[start_index:end_index]
    
    return "Index out of range"
def exit():
    print("Exiting the program...")                                                                                                                       
    
def list_game():

 fruits_list=["orange","apricot","peach","watermelon","strawberry"] 
 
while True:
    print("fruits name" ,fruits_list)

    print("Select an option:")
    print("1. fruits_access")    
    print("2. modify_fruits")
    print("3. slicing_fruits")
    print("4. exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        index = int(input("Enter the index of the fruit you want to access: "))
        print(fruits_access(fruits_list,index))
        
    elif choice == "2":
        index = int(input("Enter the index of the fruit you want to modify: "))
        new_value = input("Enter the new fruit: ")
        print(modify_fruits(fruits_list,index,new_value))
    
    elif choice == "3":
        start_index = int(input("Enter the start index for slicing: "))
        end_index = int(input("Enter the end index for slicing: "))
        print(slicing_fruits(fruits_list,start_index,end_index))
        
    elif choice == "4":
        exit()
        break
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    list_game()