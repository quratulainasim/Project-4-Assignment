import random

chars="abcdefghijklmnopqrstuvwxyz01234578910ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$&!%*"
lenght=int(input("Enter the lenght of your password: "))
password=""
for a in range(lenght):
    password+=random.choice(chars)

print(password)
