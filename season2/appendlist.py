num=[]

num.append(20)
num.append(12)
print(num)


myset=set(["rashmi","is","is","Geeks"])

print(myset)

list2=[1,2,3,4,5]

print (sum(list2)/len(list2))

list3=[1,2,2,3,4,5,6,7,8]

print()

list3 =[12, 24, 28, 31]
list4 = [9, 35, 24, 11]
list4[::-1]
print(list3,list4[::-1])

[print(x,y) for x,y in zip(list3, list4[::-1])]



list5= [1,2,3,8,8,8,4]
valueToBeRemoved = 8
result = filter(lambda val: val !=  valueToBeRemoved, list5)
print(list(result))


abcd=set(list5)
print(abcd)
if 8 in abcd:
    abcd.remove(8)
print(abcd)




