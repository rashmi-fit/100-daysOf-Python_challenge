# below program is an example of inheritance where citrus is extending some feature from fruit

class fruit:
    def __init__(self):
        print(f'i am a fruit')

class citrus(fruit):
    def __init__(self):
        super().__init__()
        print(f'i am citrus')

Lemon = citrus()
