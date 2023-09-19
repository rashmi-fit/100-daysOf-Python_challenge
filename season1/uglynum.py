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
        # temp=num
        while num % x == 0:
            num = num / x
            # print(num)
            break
            # return True
    # return True
    return True if num == 1 else False

# uglynum(1)
print(uglynum(1))