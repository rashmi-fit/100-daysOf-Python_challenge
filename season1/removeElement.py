'''
https://leetcode.com/problems/remove-element/
Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. 
The relative order of the elements may be changed.
Since it is impossible to change the length of the array in 
some languages, you must instead have the result be placed in 
the first part of the array nums. More formally, 
if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

'''
num_array=[1,2,3,4,56,6,6,7,6,8,6]
val=6

num_array.sort()
print("Before: ",num_array)
while num_array.count(val):
    num_array.remove(val)
print("After: ",num_array)
print(len(num_array))

# i=0
# while(i<len(num_array)):
#     if (num_array[i]==val):
#         num_array[i],num_array[-1]=num_array[-1],num_array[i]
#         num_array.pop()
#     else:
#         i+=1
# print(num_array)
# print(i)