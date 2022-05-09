'''
https://leetcode.com/problems/word-pattern/

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

'''


# pattern = "abba"
# s = "dog cat cat dog"
# t=s.split()
# if len(set(pattern))==len(set(zip(pattern,t)))==len(set(t)) and len(pattern)==len(t):
#     print("true")
# else:
#     print("false")


def wordPattern(p,s):
    p = "abba"
    s = "dog cat cat dog"
    p=list(p)
    s=s.split(" ")
    if len(p)!=len(s): return 0
    d={}

    for i in range(len(p)):
        if p[i] in d.keys():
                if d[p[i]]!=s[i]: return 0
        else:
            if s[i] in d.values(): return 0
            else: d[p[i]]=s[i]
    return 1
print(wordPattern("abba","dog cat cat dog"))