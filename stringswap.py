'''
https://www.geeksforgeeks.org/python-swap-elements-in-string-list/
'''
string1=["abcd","efgh","ijkl","mnop","QRST"]
print("before: ",string1)
for i in string1:
    res=i.replace('a','-').replace('Q','a').replace('-', 'Q')
    print("after: ",str(res))

# Ask aayush/i