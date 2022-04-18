'''Write a function to find the longest common prefix string amongst an 
array of strings.
If there is no common prefix, return an empty string "".
https://leetcode.com/problems/longest-common-prefix/
'''

def longcom_prefix(str):
    empty=''
    # if empty string exists
    if len(str)==0:
        return ''

    minlen=len(str[0])
    for i in range(len(str)):
        minlen=min(minlen,len(str[i]))

    for i in range(minlen):
        si=str[0][i]
        for j in range(1,len(str)):
            if str[j][i]!= si:
                return empty
        empty+=si
    return empty
 
string = ['flight', 'fklow', 'flower']
print(longcom_prefix(string))
