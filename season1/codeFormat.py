'''
code format for unm
'''
import re
# name=input("whats your name? ").strip()
# if "," in name:
#     last,first= name.split(", ")
#     name=f"{first}{last}"
# print(f"hello,{name}")

name=input("whats your name? ").strip()
matches=re.search("^.+, .+$",name)