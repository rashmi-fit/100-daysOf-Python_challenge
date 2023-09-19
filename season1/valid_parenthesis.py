'''https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
  determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
def valid_parenthesis(s:str):
  my_dict={'(': ')', '{': '}', '[' : ']'}
  open_char=[]
  for char in s:
    
    if char in my_dict.values():
      open_char.append(char)


    elif char in my_dict.keys():
      
      if open_char==[] or open_char.pop()!=my_dict[char]:
        return False

      else:
       return False

  return open_char==[]


print(valid_parenthesis("()[]{}"))
