'''
is operator vs ==
== checks value
is :check the address of the variable
'''

a=[1,2]
b=[1,2]
if a==b:
    print("a value equals with b")

if a is b:
    print("a is b")