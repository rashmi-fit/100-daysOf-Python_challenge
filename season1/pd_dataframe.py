import pandas as pd

l1=[1,2,3,4,5]

data1= pd.DataFrame(l1)
print(f'data frame1 {data1}')

dt1= {'fruit_name':['apple', 'orange', 'mango'], 'count' : [10,23,25]}


print(pd.DataFrame(dt1))