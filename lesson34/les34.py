"""
За допомогою вбудованого модуля os реалізувати простий консольний файловий менеджер. Програма має виконувати наступні дії: 
1. Виводити список вкладених файлів і папок у поточній папці.
2. Виводити розгонутий список вкладений об'єктів, рекурсивно відображаючи 
зміст усіх вкладених папок, незважаючи на глибину вкладеності. 
Вивід має бути зорганізований таким чином6 щоб наочно представляти 
вкладеність (наприклад, вкладені об'єкти зміщуються відносно батьківських на позицію табуляції)
3. Зберігати повну структуру вкалдених файлів і папок у JSON файл.
4. Створювати нові папки.
5. Переіменовувати папки.
6. Видаляти папки з усім їх змістом. Якщо заданий об'єкт не є папкою
 - не видаляти та виводити повідомлення про помилку.
7. Створювати нові файли.
8. Переіменовувати файли.
9. Переміщати файли між папками.
10. Видаляти файли. Якщо об'єкт не є файлом - виводити відповідну помилку.
11. Виконувати будь-яку додаткову дію на ваш вибір 
(наприклад, виведення додаткової інформації про файл - розмір, дата модифікації тощо).
12. Якщо при переіменуванні/переміщенні/видаленні запитаного файла або папки не існує - виводити повідомлення про помилку.
13. Послідовний список усіх дій, виконаних програмою, має зберігатися у файл log.txt у довільному форматі.
14. Кожен реалізований метод має мати щонайменше один автоматизований тест до нього.
"""
import os

# 1. Виводити список вкладених файлів і папок у поточній папці.
def current_folder():
	#print(os.listdir(path="."))
	print(os.listdir())


# 4 Створювати нові папки.
def add_new_folder(name):
	#os.mkdir(".", name)
	#os.mkdir(path = '.', name)
	os.mkdir(name)

# 5. Переіменовувати папки.
def rename_folder(old_name, new_name):
	os.rename(old_name, new_name)

# 6. Видаляти папки з усім їх змістом. Якщо заданий об'єкт не є папкою - не видаляти та виводити повідомлення про помилку.
def remove_folder(name):
	os.removedirs(name)

current_folder()
#add_new_folder("qwerty")
#rename_folder("qwerty", "qwerty2")

current_folder()
#remove_folder("qwerty")
print(os.path.isabs("qwerty"))
current_folder()



'''
ACTIONS = {
    'add': Student.add_student,
    'avg_age': calculate_avg_age,
    'load': Student.load_students,
    'print': Student.print_students,
    'dump_json': global_student_class_list.dump_json,
    'dump_csv': dump_csv,
    'load_json': global_student_class_list.load_json,
    'load_csv': load_csv
}

if __name__ == '__main__':
	while True:
        action = input('Desired action:\t')
        if action in ACTIONS:
            print('The lenght of ALL_STUDENTS list', len(Student.ALL_STUDENTS))
            ACTIONS.get(action)()
        else:
            break
'''
