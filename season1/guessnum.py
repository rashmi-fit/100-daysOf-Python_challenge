'''
https://leetcode.com/problems/guess-number-higher-or-lower/

Input: n = 10, pick = 6
Output: 6

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
'''
from random import random


import random
num=random.randrange(1,50)
guess=int(input("enter a num between 1 to 50"))


while guess!=num:
    if guess>num:
        print("-1")
        break
    elif guess<num:
        print("1")
        guess=int(input("enter a num between 1 to 50"))
    else:
        print("0")
