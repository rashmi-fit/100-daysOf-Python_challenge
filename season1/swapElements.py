'''
https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/
Given a list, write a Python program to swap first and last element of the list.

'''
l1= [1,2,3,4,5]
print("before swapping : ",l1)
length_l1=len(l1)
temp=l1[0]
l1[0]=l1[length_l1-1]
l1[length_l1-1]=temp
print("after swapping : ",l1)