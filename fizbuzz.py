
'''Given a number n, for each integer i in the range from 1 to n inclusive, print one value per line as follows:



If i is a multiple of both 3 and 5, print FizzBuzz.
If i is a multiple of 3 (but not 5), print Fizz.
If i is a multiple of 5 (but not 3), print Buzz.
If i is not a multiple of 3 or 5, print the value of i.'''

print(*['FizzBuzz' if i%3 == 0 and i%5 == 0 else 'Fizz' if i%3 == 0 else 'Buzz' if i%5 == 0 else i for i in range(1,101)], sep='\n')