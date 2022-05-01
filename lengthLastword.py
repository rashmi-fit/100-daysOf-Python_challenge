'''
https://leetcode.com/problems/length-of-last-word/

Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
edge case are can be string ,can contain only white space
'''
# entered_word="luffy is still joyboy"
# entered_word=input("enter the string")
# word=entered_word.split()
# try:  
#     print(word[-1])
#     print(len(word[-1]))
# except e:
#     print("it might have space or string is empty",e)


# one liner
entered_string=input("enter the string")
word=entered_string.split()
print("notfound") if not word else print(len(word[-1]))

