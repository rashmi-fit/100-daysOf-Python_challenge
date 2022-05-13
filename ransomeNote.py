'''
https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

def canConstruct(self, ransomNote, magazine):

        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
    if dict_magazine[char] < dict_ransomNote[char]:

        return False
        
    dict_ransomNote = defaultdict(int)
    dict_magazine = defaultdict(int)
        
    for char in ransomNote:
        dict_ransomNote[char] += 1
        
    for char in magazine:
        dict_magazine[char] += 1
            
    for char in ransomNote:
        if dict_magazine[char] > dict_ransomNote[char]:
            return False
            
    return True

canConstruct()

    # def canConstruct(self, ransomNote, magazine):
    #     """
    #     :type ransomNote: str
    #     :type magazine: str
    #     :rtype: bool
    #     """
    #     bitmap = [0]*26
    #     for i in ransomNote:
    #         bitmap[ord(i)-ord('a')] +=1
        
    #     for i in magazine:
    #         if bitmap[ord(i)-ord('a')] > 0:
    #             bitmap[ord(i)-ord('a')] -= 1
    #     return sum(bitmap) == 0