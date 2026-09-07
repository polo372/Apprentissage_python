import string
import random
user_password = ""
print()
print("Welcome to the password generator")
print()
caracteres_possibles = ""
while caracteres_possibles == "":
    user_choice = input("Do you want lowercase? y/n ")
    if user_choice == "y":
        caracteres_possibles += string.ascii_lowercase

    user_choice = input("Do you want uppercase? y/n ")
    if user_choice == "y":
        caracteres_possibles += string.ascii_uppercase

    user_choice = input("Do you want number? y/n ")
    if user_choice == "y":
        caracteres_possibles += string.digits

    user_choice = input("Do you want punctuation? y/n ")
    if user_choice == "y":
        caracteres_possibles += string.punctuation
    if caracteres_possibles == "":
        print("*" * 30)
        print("you need to choose one option")
        print("*" * 30)
length = int(input("What was the length of your password ? "))
for i in range(length):
    rand = random.choice(caracteres_possibles)
    user_password += rand
print(f"Your password : {user_password}")


