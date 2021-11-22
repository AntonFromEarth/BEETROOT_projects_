
'''
#1. Відсортувати тварин за віком
'''
animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5},
]
arr = sorted([age['age'] for age in animals])
#print("arr = ", arr)
animal_list = []
for age in arr:
    for animal in animals:
        if age == animal['age']:
            animal_list.append(animal)

print(animal_list)

'''
#1.2
animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5},
]
n=len(animals)
for i in range(n-1):
    for j in range(0, n-i-1):
        if animals[j]['age'] > animals[j+1]['age']:
            animals[j]['age'], animals[j+1]['age'] = animals[j+1]['age'], animals[j]['age']
print(animals)
'''


'''
#2. З використанням list comprehension cтворити список квадратів непарних елементів вхідного списку numbers
numbers = [4, 2, 1, 6, 9, 7]
'''
numbers = [4, 2, 1, 6, 9, 7]
a = [i**2 for i in numbers if i%2 != 0]
print(a)

'''
#3. Реалізувати функцію послідовного пошуку, який шукає потрібний елемент, починаючи з кінця вхідного списку
names = ['Joe', 'Mary', 'Ann', 'Andrew', 'Stephan', 'Rosie']
element_to_find = 'Stephan'
'''
def my_find(names, element):
    for index in range(len(names)-1, 0, -1):
        if names[index] == element:
            return index
    return None

names = ['Joe', 'Mary', 'Ann', 'Andrew', 'Stephan', 'Rosie']
element_to_find = 'Stephan'

print(my_find(names, element_to_find))


'''
4. Реалізувати клас Container, який відповідає наступним умовам:
   - кожен об'єкт цього класу має атрибут elements, який при створенні нового об'єкту класу є пустим списком
   - об'єкт має метод add(), який додає новий елемент до списку
   - тип елементів, що можуть зберігатися у контейнері, визначається за першим доданим елементом: якщо першим 
   було додано int, всі наступні мають бути int. Якщо першим було додано str, всі наступні також str. 
   Модливі типи даних - примітивні типи мови Python (без колекцій та мапінгів)
   Якщо ця умова не виконується - метод add повертає помилку TypeError
   - elements завжди відсортовано за зростанням
'''  

class Container:



    def __init__(self):
        self.elements = []
        self.fu_type = None

    def add(self, new_elem):
        if self.elements == []:
            self.fu_type = type(new_elem)
            self.elements.append(new_elem)
        elif type(new_elem) == self.fu_type:
            self.elements.append(new_elem)
            temp = sorted(self.elements)
            self.elements = temp
        else:
            raise TypeError ("Wrong!!!")

obj_1 = Container()
obj_2 = Container()


obj_1.add(5)
obj_2.add('5')
print(obj_1.elements)
print(obj_2.elements)

obj_1.add(1)
obj_2.add('1')
obj_1.add(3)
obj_2.add('3')
print(obj_1.elements)
print(obj_2.elements)
