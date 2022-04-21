'''
https://leetcode.com/problems/palindrome-number/
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

'''
pali_num=121
str_pali_num=str(pali_num) 
# converting to string and using slicng
if str(pali_num)==str(str_pali_num[::-1]):
    print("palindrome")
else:
    print("not palindrome")