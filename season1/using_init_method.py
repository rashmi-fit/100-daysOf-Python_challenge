# Below program is made using the init constructor in python
class student:
    def __init__(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch
    def print_student(self):
        print(f'name :{self.name}')
        print(f'age :{self.age}')
        print(f'branch :{self.branch}')

student1= student("rashmi",12,"doctor")
student1.print_student()
