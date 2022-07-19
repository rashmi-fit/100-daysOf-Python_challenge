num=int(input("what is the multiplication table you want "))

mx= [(x+1)*num for x in range(20)]
mx2= [str(x+1) + 'x' +  str(num) +'=' + str((x+1)*num) for x in range(20)]
mx3= [f' {x+1} x {num} = {(x+1)*num} ' for x in range(20)]

print(mx)
print(mx2)
print(mx3)
