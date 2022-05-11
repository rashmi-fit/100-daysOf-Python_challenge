'''
Given an integer n, return true if it is a power of three. Otherwise, return false.
https://leetcode.com/problems/power-of-three/

An integer n is a power of three, if there exists an integer x such that n == 3x.
'''

num=int(input("enter a number: "))

# while True:
#     if num!=0 and num%3==0:
#         print(f"true {num}")
#         break
#     else:
#         print(f"false {num}")
#         break

if num==0:
    print(f"false {num}")

while num!=1:
    if num%3!=0:
        print(f"false {num}")
    num=num//3
print(f"true {num}")