"""
This program will identify how many items the user guess the number

"""
import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range<=0:
        print(f'Please type a number larger than 0 next time!')
        quit()
else:
    print(f'Please type a number next time.')
    quit()


random_number = random.randint(0,top_of_range)
guesses=0
while True:
    guesses+=1
    user_guess= input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print(f'Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print(f"you were above the number ")
    else:
        print(f"you are below the number")

print(f'You got it in {guesses} guesses')