exp=-1
total=0
maxexp=0
minexp=0
while exp!=0:
    exp= int(input("what is the expense? (type 0 to stop) "))
    total=total+exp
    if exp>maxexp:
        maxexp=exp
    elif exp>minexp and exp<maxexp:
        minexp=exp
    else:
        print("something wrong happened!")
print("Your total expenditure is "+ str(total))
print("Your max expenditure is "+ str(maxexp))
print("Your min expenditure is "+ str(minexp))
