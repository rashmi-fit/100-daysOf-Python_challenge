'''
https://www.geeksforgeeks.org/maximum-of-two-numbers-in-python/?ref=leftbar-rightbar
Given two numbers, write a Python code to find the Maximum of these two numbers.
'''
# a=int(input("enter 1st num"))
# b=int(input("enter 2nd num"))
# if a>b: print("max is: ",a) 
# else: print("max is: ",b)


a=int(input("enter 1st num"))
b=int(input("enter 2nd num"))
print(a if a >= b else b)