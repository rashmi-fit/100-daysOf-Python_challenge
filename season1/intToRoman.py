'''
integer to roman
Logic :
find the largest number from the list <=your number
yournum-largestnum= remaining
remaining is less than someother number and continue
'''

numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
roman = ['I','IV','V','IX', 'X','XL', 'L','XC', 'C','CD', 'D','CM','M']
roman_numeral=''
index=12
# i have total 13 characters in the roman and numbers
entered_num=int(input("enter number"))

# if entered num is not zero
while entered_num!=0:
    if numbers[index] <= entered_num:
     roman_numeral+=roman[index]
     entered_num=entered_num-numbers[index] 
    #  if num less than or eaqual to etered num

    else:
        index-=1
print(roman_numeral)

