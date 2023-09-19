'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

'''

output=[]
def rec(l,r,stack,cand):
    if l==r==0:
        output.append(cand)
    if l >0:
        rec(l-1,r,stack+1,cand+"(")
    if r>0 and stack >0:
        rec(l,r-1,stack-1,cand+")")
    rec(n,n,0,"")
    return output

