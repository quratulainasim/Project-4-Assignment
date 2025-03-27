PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():

    user_age:int = int(input("Enter your age: "))

    if user_age >= PETURKSBOUIPO_AGE:

        print("Peturksbouipo can vote.")
    else:
        print("Peturksbouipo cannot vote.")

    if user_age >= STANLAU_AGE:
        print("Stanlau can vote.")
    else:
        print("Stanlau cannot vote.")

    if user_age >= MAYENGUA_AGE:
        print("Mayengua can vote.")

    else:
        print("Mayengua cannot vote.")

if __name__ == '__main__':
    main()        