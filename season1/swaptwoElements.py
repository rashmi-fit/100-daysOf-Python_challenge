'''
https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/
Given a list in Python and provided the positions of the elements, 
write a program to swap the two elements in the list.
'''
list1=[1,2,3,4,5,6,7]
print("before :", list1)
pos1=4
pos2=5
temp=0
len_list1=len(list1)
temp=list1[pos1]
list1[pos1]=list1[pos2]
list1[pos2]=temp
print("after :", list1)