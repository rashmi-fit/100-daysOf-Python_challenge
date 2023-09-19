import random
def isDDM(a, n) :
 
    # for each row
    for i in range(0, n) :        
     
        # for each column, finding
        # sum of each row.
        sum = 0
        for j in range(0, n) :
            sum = sum + abs(a[i][j])    
 
        # removing the
        # diagonal element.
        sum = sum - abs(a[i][i])
 
        # checking if diagonal
        # element is less than
        # sum of non-diagonal
        # element.
        if (abs(a[i][i]) < sum) :
            return False
 
    return True
 
# Driver Code
# n = 4
# m = [[ 3, -2, 1,4 ],
#     [ 1, -3, 2,4 ],
#     [ -1, 2, 4,4 ],
#     [ -1, 2, 4,5 ]]

n = 4
columns = 4
a= [[random.randrange(22, 37, 2) for x in range(columns)] for y in range(n)]
print([[random.randrange(22, 37, 2) for x in range(columns)] for y in range(n)])
 
if((isDDM(n, a))) :
    print ("YES")
else :
    print ("NO")