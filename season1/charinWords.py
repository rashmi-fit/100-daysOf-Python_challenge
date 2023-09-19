import pandas as pd

ser=pd.Series(["rashmi","is", "a", "good", "coder"])

print(ser.map(lambda a:len(a)))