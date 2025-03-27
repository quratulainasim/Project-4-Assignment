def get_number(list):
    print(list[0])

def user_get():
    list = []
    user_input:str = input("Enter a number:")
    while user_input != "":
        list.append(user_input)
        user_input:str = input("Enter a number:")
    return list 
def main():
    list = user_get()
    get_number(list)
if __name__ == "__main__":
    main()