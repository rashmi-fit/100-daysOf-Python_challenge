#create 100numbers in python
import random as rdm
#generate a list of numbers between 1 and 25
list_of_nums = [rdm.randint(1,26) for i in range (10)] #range is exclusive at
print(f'The generated list: {list_of_nums}')


