'''
Purpose: create two object with attributes like brand_name, model_name, price
'''
class Laptop:
      def __init__(self, brand_name, model_name, price) :
            self.brand_name = brand_name
            self.model_name = model_name
            self.price = price

l1 = Laptop('BMW', 'BM-1234', '1765£')
l2 = Laptop('Range-Rover', 'RR-1234', '12765£')

print(f'brand_name: {l1.brand_name}')
print(f'brand_name: {l2.brand_name}')
print(f'')

print(f'brand_name: {l1.model_name}')
print(f'brand_name: {l2.model_name}')

print(f'')
print(f'brand_name: {l1.price}')
print(f'brand_name: {l2.price}')
