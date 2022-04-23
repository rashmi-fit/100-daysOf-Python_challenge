'''Anagram is something if you rearange it has some meaning

'''
def is_anagram(s1, s2):
    return set(s1) == set(s2)
print(is_anagram("elvis", "lives"))