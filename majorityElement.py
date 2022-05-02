'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
https://leetcode.com/problems/majority-element/
'''
list1=[2,1,1,1,1,2,2]
# list1=int(input("enter numbers only in this list"))
majority=len(list1)/2
dict_freq={}
for num in list1:
    if num not in dict_freq:
        dict_freq[num]=1
    else:
        dict_freq[num]+=1

for digit in dict_freq:
    if dict_freq[digit]> majority:
        print(digit)

