# l=[]
# for num in range(100):
#      l.append(num)

# below is list comprehension
l= [num for num in range(10)]
even_num= [num*2 for num in range(10)]

print(l)
print(even_num)
print(even_num[7])
print("last item: ",even_num[-1])
print("3rd last item: ",even_num[-3])
print("slicing: ", even_num[3:])