def compute_fact(number):
    fact=1
    while number>0:
        fact=fact*number
        number=number-1
    return fact
print("factorial of 5 is",compute_fact(3))