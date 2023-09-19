''' . Isomorphic Strings
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, 
but a character may map to itself.
'''
# def reduce(s):
#     result = []
#     lookup = {}
#     for i, c in enumerate(s):
#         if c in lookup:
#             result[lookup[c]].append(i)
#         else:
#             result.append([i])
#             lookup[c] = len(result)-1
#     return result
    

# class Solution(object):
#     def isIsomorphic(self, s, t):
#         return reduce(s) == reduce(t)

def isIsomorphic(self, s: str, t: str, second: bool = False) -> bool:
        
        morph = {} # character map
        
        # just checking if morphs are all identical
        for i, first in enumerate(s):
            if first in morph:
                if t[i] != morph[first]:
                    return False
            else:
                morph[first] = t[i]
        
        # check the other way round if it's not the second check
        return (True if second else self.isIsomorphic(t, s, True))