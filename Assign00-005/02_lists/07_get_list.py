def get_list():
    list = []
    user_input = input("Enter a value :")
    while user_input:
        list.append(user_input)
        user_input = input("Enter a value :")
    print("Complete list:", list)
if __name__ == "__main__":
    get_list()
    