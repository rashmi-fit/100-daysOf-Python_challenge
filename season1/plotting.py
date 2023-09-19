# create a simple plot where x and y axis value range from o-10

import numpy as np
from matplotlib import pyplot as plt

x=np.arange(0,10,1)
print(x)

y=np.arange(0,10,1)
print(y)

plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("X vs Y")