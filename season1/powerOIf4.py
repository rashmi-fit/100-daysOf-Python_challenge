'''
https://leetcode.com/problems/power-of-four/
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x
'''

num=int(input("enter a number: "))
if num==0:
    print(f"false {num}")

while num!=1:
    if num%4!=0:
        print(f"false {num}")
    num=num//4
print(f"true {num}")

