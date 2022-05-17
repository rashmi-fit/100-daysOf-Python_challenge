'''
ternary or conditional operator

x+y =>binary operatory
x=firstval if condition else second value =>ternary operator  3 arguments
find max of two given numbs
'''
# x= int(input("enter first two val"))
# y= int(input("enter second two val"))

# maxval= x if x>y else y
# print(f"max value is: {maxval}")


a= int(input("enter first two val"))
b= int(input("enter second two val"))
c= int(input("enter third two val"))

biggestvalue= a if a>b and a>c else b if b>c else c
print(f"biggestvalue is: {biggestvalue}")
# nesting of ternary is possible