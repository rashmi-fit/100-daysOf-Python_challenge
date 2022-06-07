'''
Given a text file file.txt, print just the 10th line of the file.

Example:

Assume that file.txt has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
'''

userinput= input("enter the text")

file= open("https://github.com/rashmi-fit/100-daysOf-Python_challenge/blob/main/file.txt",'r')

for line in file:
    if userinput in line:
        print(line)