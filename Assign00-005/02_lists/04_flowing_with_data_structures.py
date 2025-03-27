def copy_data(data,list):
    for i in range(3):
        list.append(data)
def main():
    user_message = input("Enter a message :")
    list =[]
    print("LIST BEFORE COPY:",list)
    copy_data(user_message,list)
    print("LIST AFTER COPY:",list)
if __name__ == "__main__":
    main()            