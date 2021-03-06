"""
1. Чи правильне твердження, що Python - нетипізована мова програмування? Наведіть приклад коду, 
який підтвердить або спростує це твердження.

2. Яка різниця між мутебальними та імутабельними типами даних у Python? Наведіть короткий приклад коду,
який ілюструє цю різницю

3. У чому полягає принцип "duck typing"? Наведіть приклад застосування цього принципу

4. Які типи даних можуть бути ключами у dict?

5. У чому полягає різниця між set та frozen set?

6. Перерахуйте основні принципи ООП.

7. Наведіть приклад коду, який демонструє принцип спадкування

8. Створіть декоратор, який заміряє час виконання задекорованої функції. 
Декоратор не обмежує кількість та порядок аргументів, що передаються функції. 
Декоратор має у циклі викликати задекоровану функцію 1000 разів, а після того виводити 
 рядок з назвою функції, її аргументами, часом виконання 1000 викликів. 
Декоратор має повертати результат останнього, тисячного, виклику функції.

9. Реалізувати функцію eucledian_gcd(a: int, b: int) -> int, яка обраховуватиме найбільший
 спільний дільник для агрументів a та b за алгоритмом Евкліда. 

Алгоритм Евкліда для пошуку НСД:
    1) Допоки a != b:
        - якщо a > b, то a = a - b
        - якщо b > a, то b = b - a
    2) Коли a == b, повертаємо а, яке і буде найбільшим спільним дільником.

10. З модулю math імпортувати функцію gcd, яка обраховує набільший спільний дільник.

11. Задекорувати функції з завдань 9 та 10 декоратором з завдання 8.

12. Викликати кожну задекоровану функцію з завдання 11 з аргументами:
    1) a = 30, b = 6
    2) a = 100, b = 1
    3) a = 999, b = 9
    4) a = 4, b = 1024

    Навести результат виконання задекорованих функцій, зробити висновок про швидкість
     роботи кожної з задекорованих функцій.
"""

from functools import wraps

def my_decorator(*args, **kwargs):
    print('My decorator')
    def actually_decorator(func):
        print('Actuall a decorator')
        @wraps(func)
        def wrapper(*func_args, **func_kwargs):
            print('This is wrapper')
            func(*func_args, **func_kwargs)
        return wrapper
    return actually_decorator
 
def counter(func):
    @wraps(func)
    def wrapper(*args):
        wrapper.runs += 1
        func(*args)
        print('Successful runs: {}'.format(wrapper.runs))
    wrapper.runs = 0
    return wrapper

def log(func):
    def wrapper(*args):
        res = func(*args)
        print(res)
        print(*args)
        return res
    return wrapper

def decorator1(func):
    def wrapper(*args):
        print('Decorator 1 before func')
        func()
        print('Decorator 1 after func')
    return wrapper

def decorator2(func):
    def wrapper(*args):
        print('Decorator 2 before func')
        func(*args)
        print('Decorator 2 after func')
    return wrapper

#@decorator1
#@decorator2
@my_decorator('This is Spartaaaaa!')
def say_hello():
    print('Hello World')

say_hello()
say_hello()
say_hello()

#@counter()
#def dummy(*args):
#    pass

#@counter
#@log
#def sum_two_numbers(a, b):
#    return a + b

#s = sum_two_numbers(6, 7)
#print(s)
#say_hello('World')
#print(say_hello.__name__)
#print(dummy.__name__)