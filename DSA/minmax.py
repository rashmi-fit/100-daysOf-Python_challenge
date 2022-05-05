'''
https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
Your Task:  
You don't need to read input or print anything. 
Your task is to complete the function getMinMax() which takes the array A[] and
 its size N as inputs and returns the minimum and maximum element of the array.

ask aayush/i
'''

def getMInMax(a,n):
    arr_max, arr_min= a[0],a[0]
    for i in range(n):
        if arr_max<a[i]:
            arr_max=a[i]
            # print("max: ",arr_max)
        elif arr_min >a[i]:
            arr_min=a[i]
            # print("min :",arr_min)
    return arr_min, arr_max

array1=[1,2,3,4,5,6]
num=5
getMInMax(array1,num)
