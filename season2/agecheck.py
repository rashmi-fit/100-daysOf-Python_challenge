name=input("what is your name?")
age= int(input("how old are you?"))

yearsto50= 50-age

if yearsto50>0:
    print(f"hello {name} ,you will be {str(yearsto50)} years")
else:
    print(f'hello {name} ,you will be {str(-yearsto50)} years ago')
print(f'Bye')