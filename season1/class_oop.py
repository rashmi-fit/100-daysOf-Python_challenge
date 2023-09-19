class human:
    name = None
    age = None
    def get_name(self):
        print("Enter your name:")
        self.name=input()
    def get_age(self):
        print("Enter your age: ")
        self.age=input()
    def put_name(self):
        print(f'your name is {self.name}')
    def put_age(self):
        print(f'your age is {self.age}')

person1= human()
person1.get_name()
person1.get_age()
print(person1.put_age() ,person1.put_name())