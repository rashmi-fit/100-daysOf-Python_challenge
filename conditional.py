'''
Write a program that utilizes the concept of conditional execution, takes a string as input, and:

    prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen 
    if the inputted string is "Spathiphyllum" (upper-case)
    prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
    prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.


Test your code using the data we've provided for you. And get yourself a Spathiphyllum, too!

'''
string=input("enter a string")
compare= "Spathiphyllum"
if string == compare.upper():
    print("Yes - Spathiphyllum is the best plant ever!")
if string == compare.lower():
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not [input]!")