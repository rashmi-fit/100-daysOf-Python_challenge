'''
https://practice.geeksforgeeks.org/problems/reverse-an-array/0#

Given an array A of size N, print the reverse of it.
Check with aayush/i
'''

t = int(input("enter numbers: "))
n = int(input())
for i in range(t):

    arr = input().split()
    # print(arr)
print(" ".join(arr[::-1]))