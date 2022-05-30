'''learning with python and json'''

import json
 
# {key:value mapping}
a ={"name":"Rashmi",
   "age":31,
    "Salary":"20k"}
 
# conversion to JSON done by dumps() function
b = json.dumps(a)
 
# printing the output
print(b)