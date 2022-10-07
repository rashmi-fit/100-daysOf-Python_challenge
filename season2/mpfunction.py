def calculateSq(n):
    return n*n
numbers = (2, 3, 4, 5)
result = map(calculateSq, numbers)
print(result)