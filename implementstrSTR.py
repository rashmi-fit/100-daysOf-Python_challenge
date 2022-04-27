'''
https://leetcode.com/problems/implement-strstr/
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
Clarification:

What should we return when needle is an empty string? 
This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when 
needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

'''
haystack=input("enter a string1: ")
needle=input("enter string2: ")
if not needle:
    print(0)
for i in range(len(haystack)):
    if haystack[i:i+len(needle)]==needle:
        print(i)
print(-1) 
# its not the firstindex of occurance so printing -1


