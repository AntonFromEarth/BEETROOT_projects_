class Cat_1:
    def __init__(self, name):
        self.name = name

class Cat_2:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"{self.__class__}: {self.name}"

class Cat_3:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"{self.__class__}: {self.name}"
    def __str__(self):
        return f"{self.name}"

cat_1 = Cat_1('Васька')
print(cat_1)
cat_2 = Cat_2('Барсик')
print(cat_2)
cat_3 = Cat_3('Пушок')
print(cat_3)

cat_list = [cat_1, cat_2, cat_3]
print("cat_list = ", cat_list)
