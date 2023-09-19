'''
url
'''

import re
# url= input("URL: ").strip()

# username= re.sub("^(https?://)?(www\.)?twitter\.com/","",url)

# print(f"usernmae:{username}")

url=input("URL: ").strip()

if matches:= re.search("^https?://(?:www\.)?twitter\.com/([a-z0-9_]+))", url, re.IGNORECASE):
    print(f"username:",matches.group(1))