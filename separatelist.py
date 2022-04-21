'''
Given a list separate out the numbers and string
'''
list=[1,2,'a','b',3,'c']
empty_list=[]
str_list=[]
for i in list:
    if type(i) is int or type(i) is float:
        empty_list.append(i)
    else:
        if i.isnumeric():
             empty_list.append(i)
        
        else:
            str_list.append(i)
            # print(i,"is not integer") 
print(empty_list)
print(str_list)
