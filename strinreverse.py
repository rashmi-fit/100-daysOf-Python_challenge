'''
 Write a code snippet thta asks a user for their name and 
 print the name in following pattern B Bi Bil Bill
'''

name=input("enter youe name :")
for i in range(len(name)):
    print(name[:i+1], end=" ")