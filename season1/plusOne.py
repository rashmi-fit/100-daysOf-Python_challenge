'''
https://leetcode.com/problems/plus-one/
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. The digits are ordered from most 
significant to least significant in left-to-right order. The large integer does not contain 
any leading 0's.
Increment the large integer by one and return the resulting array of digits.
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
'''

list1=[1,2,3]
digit=list1[::-1]
one,i=1,0
while one:
    if i<len(digit):
        if digit[i]==9:
            digit[i]=0
        else:
            digit[i]+=1
            one=0
    else:
        digit.append(1)
        one=0
    i+=1
print(digit[::-1])

