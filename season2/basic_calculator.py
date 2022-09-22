def addition(num1, num2):
    return num1+num2

def subsctraction(num1, num2):
    return num1-num2

def multiply(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1/ num2


print("Please select operations\n " \
      "1. Add\n " \
      "2. Substract\n" \
      "3. Multiply\n" \
      "4. Divide\n" )


select= int(input(f"select the operations from 1, 2, 3,4 "))
number1= int(input("enter the num1"))
number2= int(input("enter the num2"))

if select ==1:
    print(f'num1+num2= {addition(number1,number2)}')

elif select==2:
    print(f'num1-num2 {subsctraction(number1,number2)}')

elif select ==3:
    print(f'num1 *num2 {multiply(number1,number2)}')

elif select ==4:
    print(f'num1/num2 {division((number1,number2))}')
else :
    print(f'invalid input')
