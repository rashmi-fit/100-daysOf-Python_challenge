'''
identify if email id is valid
'''
import re
email=input("whats your email id? ").strip()
# if "@" in email and "." in email:
#     print("valid")
# else:
#     print("invalid")

# username,domain= email.split("@")

# if username and ("." in domain):
#     print("Valid")
# else:
#     print("Invalid")

if re.search("^\w+@\w+\.(com|gmail|edu)$",email,re.IGNORECASE):
    print("valid")
else:
    print("Invalid")

# ^ start of the string match, $ end with the pattern