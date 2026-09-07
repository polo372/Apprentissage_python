import random
random_number = (random.randint(1, 100))
round = 0
user_choice = int(input("Guess a number between 1 and 100: "))
is_running = True
while is_running:
    if user_choice == random_number:
        round +=1
        print(f"You got it in {round} guesses!")
        replay = input("Replay (y/n)?")
        if replay == "y":
            round = 0
            random_number = (random.randint(1, 100))
            user_choice = int(input("Guess a number between 1 and 100: "))
        else: 
            is_running = False
            print("thank's for playing !")
            break
    elif user_choice < random_number:
        round +=1
        print("Too low. Try again.")
        user_choice = int(input("Guess a number between 1 and 100: "))
    else:
        round +=1
        print("Too high. Try again.")
        user_choice = int(input("Guess a number between 1 and 100: "))
