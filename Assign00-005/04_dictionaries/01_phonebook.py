def add():
    phonebook = {}
    while True:
        name = input("Enter a name: ")
        if name == "":
            break
        number = input("Enter a number: ")
        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(str(name) + " : " + str(phonebook[name]))

def check_name(phonebook):
         while True:
            name = input("Enter name to check: ")
            if name == "":  
              break
            if name in phonebook: 
               print(f"{name} : {phonebook[name]}")
            else:
                 print(f"{name} is not in the phonebook.")
               
               
def main():
    phonebook = add()
    print_phonebook(phonebook)
    check_name(phonebook)         
if __name__ == "__main__":
    main()