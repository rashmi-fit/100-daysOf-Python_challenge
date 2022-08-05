# using recursion

import time
import matplotlib.pyplot as plt

def fib(n):
    if n <= 0: # base case 1
        return 0
    if n <= 1: # base case 2
        return 1
    else: # recursive step
        return fib(n-1) + fib(n-2)

numbers = 20