# using dynamic programming

def permute(LIST):
    length=len(LIST)
    if length <= 1:
        yield LIST
    else:
        for n in range(0,length):
            for end in permute( LIST[:n] + LIST[n+1:] ):
                yield [ LIST[n] ] + end

for x in permute(["3","2","1"]):
    print(x)
    xs=[int(_x_int) for _x_int in x]
    if sum(xs) > 6:
        print("bulshit")
        # break
    else:
        if x in xs:
            print("i dont know")
