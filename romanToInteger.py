''' https://leetcode.com/problems/roman-to-integer/ '''
'''back to front
Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''
def romanToInteger(string):

    my_dict={ "I"   :  1,'V': 5,'X': 10,'L' : 50,'C' : 100,'D' : 500,'M' : 1000 }
    print(my_dict)
    output=0
    N=len(string)
    i=N-1
    while i>=0:
        # check the previous is more than current one
        if i < N-1 & my_dict[string[i]] < my_dict[string[i+1]] : 
            output= output - my_dict[string[i]]
            # print("output")
        else:
            output=output+ my_dict[string[i]]
            i-=1
    return output
 
print(romanToInteger('III'))