import random

user_wins=0
computer_wins=0
options=["Rock","Paper","Scissors"]

while True:
    user_input= input("type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input =='q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
#     rock: 0 ,paper:1, scissors:2
    computer_pick= options[random_number]
    print(f'computer picked {computer_pick}')

    if user_input =="rock" and computer_pick =="scissors":
        print(f'you won!')
        user_wins+=1
        continue
    elif user_input =="paper" and computer_pick =="rock":
        print(f'you won!')
        user_wins+=1
        continue
    elif user_input =="scissors" and computer_pick =="paper":
        print(f'you won!')
        user_wins+=1
        continue
    else:
        print(f'You lost!')
        computer_wins+=1

print(f'You won {user_wins} times')
print(f'The computer won {computer_wins} times')
print("Goodbye!")

