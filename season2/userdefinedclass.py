
'''class is user defined class and used to access more informations'''
class A:
    param1= "ras"
    param2="rashu"
    def fun(self):
        print(f'i am {self.param1}')
        print(f'i am {self.param2}')

obj= A()
print(obj.param1)
obj.fun()