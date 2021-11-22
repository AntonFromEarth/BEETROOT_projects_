class Cat_1:
    def __init__(self, name):
        self.name = name


class Cat_2:
    def __init__(self, name):
        self._name = name
    @property
    def cat_name(self):
        print("in getter")
        return self._name
    

class Cat_3:
    def __init__(self, name):
        self.name = name

    @property
    def cat_name(self):
        print("in getter")
        return self.name

    @cat_name.setter
    def cat_name(self, new_name):
        print("in setter")
        self.name = new_name



cat_1 = Cat_1('Васька')
print(cat_1.name)
print()

cat_2 = Cat_2('Барсик')
print(cat_2._name)
cat_2._name = 'hfgfgf'
print(cat_2._name)
print()

cat_3 = Cat_3('Пушок')
print(cat_3.name)
cat_3.name = 'cdfdg'
print(cat_3.name)