'''
Given an integer array nums, return true if any value appears 
at least twice in the array, and return false if every element is distinct.
'''
# num_array=[1,2,3,4,5,6]
num_array=[1,1,1,2,3,4,5,6]
num_array.sort()
print(num_array)
for i in num_array:
    if i == num_array[i-1]:
        print("True",i)
    else:
        print("False")

# need to check