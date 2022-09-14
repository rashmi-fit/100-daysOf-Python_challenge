'''yield keyword returns the number of gerenators'''

def yieldfun():
    s=0
    for i in range(10):
        s+=1
        yield s
for i in yieldfun():
    print(i)