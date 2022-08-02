# convert things into title case

import pandas as pd

ser=pd.Series(['mary','had','a','little','lamb'])

print(ser)

ser=ser.map(lambda x:x.title())

print(ser)