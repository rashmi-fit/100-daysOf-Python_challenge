'''
https://leetcode.com/problems/ugly-number/
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.


'''
def uglynum(num):
    num=int(input("enter a num"))

    if num <= 0:
        return False 
    for x in [2, 3, 5]:
        while num % x == 0:
            num = num / x
            print(num)
            # return True
    return True

uglynum(1)