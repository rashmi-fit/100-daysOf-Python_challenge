'''
https://leetcode.com/problems/merge-two-sorted-lists/
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list
'''

list1=[1,3,4]
list2=[1,3,4]
list1.extend(list2)
list1.sort()
print(list1)