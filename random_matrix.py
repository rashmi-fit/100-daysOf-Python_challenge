import random
rows = 4
columns = 4
print([[random.randrange(22, 37, 2) for x in range(columns)] for y in range(rows)])