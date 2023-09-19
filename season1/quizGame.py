"""
This project will ask customer to enter the games and it will verify with the answers
The user can see the number of answers right and its percentage. Its a quiz game

"""

print(f"Welcome to my computer quiz!")

playing= input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print(f'okay! Lets Play:')
score= 0

answer= input("What does CPU stand for? ").lower()
if answer == "Central processing unit":
    print(f'Correct!')
    score += 1
else:
    print(f'Incorrect!')

answer= input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print(f'Correct!')
    score += 1
else:
    print(f'Incorrect!')

answer= input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print(f'Correct!')
    score += 1
else:
    print(f'Incorrect!')

answer= input("What does PSU stand for? ").lower()
if answer == "Power supply unit":
    print(f'Correct!')
    score += 1
else:
    print(f'Incorrect!')

print(f'You got: {score} questions correct!')
print(f'You got: {score/4*100}% correct!')

