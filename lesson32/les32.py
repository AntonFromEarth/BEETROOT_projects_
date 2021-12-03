'''
1. Створити функціонал, який ітеруватиме числа від 1 до 20:
    - за допомогою класа-ітератора;
    - за допомогою вираза-генератора (generator expression);
    - за допомогою функції-генератора (generator function).
2. Cтворити дві функції, які перевірятимуть, що заданий рядок є паліндромом 
(читається однаково в обох напрямках, без урахування пробілів). 
Перша функція має використати ітеративний підхід (через цикл), друга - рекурсивний.
3. Перерахуйте та наведіть приклади якумога більшої кількості варіантів копіювання списку.
4. Перерахуйте та наведіть приклади якумога більшої кількості варіантів створення словників.
5. Створіть функцію, яка повертає довжину рядка, отриманого як аргумент. 
До неї створіть декоратор, який явно перетворює аргумент на рядок перед 
передаванням його задекорованій функції. Задекоруйте функцію через виклик 
декоратора та через синтаксис '@'. Поясніть, що таке декоратор. 
Завдяки чому можливо використання декораторів?
6. Створіть клас, на прикладі методов якого покажіть два варіанти декоруання
 методів класу декоратором property. Поясніть функціонал декоратора property
7. Наведіть приклади отримання підрядка з рядка за індексами та з використанням об'єкту слайса
8. Наведіть два приклади варіантів коректної роботи з файлом,
 коли закриття файлу після читання буде гарантоване
9. Наведіть приклади двух функцій пошуку елементу у списку.
 Яку складність має кожен з них? Які обмеження у кожного з них?
10. Створіть клас, який ілюструє можливіть створення нових
 об'єктів двома методами: через звичний __init__ та додатковий метод класу.
  Покажіть варіанти використання кожного з них.
'''

########### \/  IGOR  \/ ##############

# expression = (i for i in range(1,20))
#
# print(next(expression))
# print(next(expression))
# print(next(expression))
# print(next(expression))
# print(next(expression))





# def generator_function(num):
#
#     print(num)
#     while num > 0:
#         yield num
#         num -= 1
#
#
# it = generator_function(5)
# #print(it)
# next(it)
# next(it)
# next(it)

# class Iterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return self.counter
#         else:
#             'stop'
#
#
#
#
# it = Iterator(20)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

########### /\  IGOR  /\ ##############


def if_polind(arg):
    flag = 1
    if type(arg) != str:
        arg = str(arg)
        #print(arg)
    
    #print(arg)
    if len(arg)%2 == 0:
        for symb in range(len(arg)/2):
            if arg[symb] == arg[symb*(-1)-1]:
                continue
            else:
                flag = 0
                break
    if len(arg)%2 == 1:
        for symb in range(int(len(arg)/2)):
            if arg[symb] == arg[symb*(-1)-1]:
                #print("arg[symb]",arg[symb])
                #print("arg[symb*(-1)-1]",arg[symb*(-1)-1])
                continue
            else:
                flag = 0
                break
    if flag:
        return True
    else:
        return False





polin_num = 12321
polin_string = 'qwertrewq'
not_poli_1 = 12345

print(if_polind(12321))
print(if_polind('qwertrewq'))
print(if_polind(12345))
print(if_polind('12345'))
