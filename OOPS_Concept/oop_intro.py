# class
# init method
# attributes, instance variables
#  create object

class Person:
      def __init__(self, first_name,last_name, age):
            # decclare the instance variables
            print(f'init method // constructor get called here')
            self.first_name = first_name
            self.last_name = last_name
            self.age = age

p1= Person('rashmi', 'mohapatra', 45)
p2= Person('liti', 'mohapatra', 40)

print(p1.first_name)
print(p2.first_name)
