MAX_LENGTH = 3
def shorten(list):
    while len(list) > MAX_LENGTH:
        store_list = list.pop()
        print(store_list)

def get_list():
    list = []
    user_input = input("Enter a value :")

    while user_input != "":
        list.append(user_input)
        user_input = input("Enter a value :")
    return list

def main():
    list = get_list()
   
    shorten(list)
 

if __name__ == "__main__":
    main()