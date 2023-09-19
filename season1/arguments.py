''' this will help me in knowing the diff between args and kwargs
https://www.geeksforgeeks.org/args-kwargs-python/?ref=lbp '''

# def myFun(*argv): 
#     for arg in argv: 
#         print (arg)
    
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 

# def myFun(**kwargs): 
#     for key, value in kwargs.items():
#         print ("%s == %s" %(key, value))
  
# # Driver code
# myFun(first ='Geeks', mid ='for', last='Geeks')

def myFun(*args,**kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
  
  
# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")