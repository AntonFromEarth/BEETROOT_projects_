'''

# 3 
ДЗ від 18.09.2021:
1. У проекті LMS створити класи Student (переймає всі атрибути зі словника student) 
 та  Group(список студентів та назва групи). Розділити наявні функції на методи цих двох класів.
2. Документацію по класах https://docs.python.org/3/tutorial/classes.html 
 читати/усвідомлювати до пункта 9.7 включно.
3. У Beetroot LMS опрацювати уроки 12, 13.
4. Збережіть на майбутнє посилання на офіційний 
 документ по Python MRO: https://www.python.org/download/releases/2.3/mro/

 ДЗ від 22.09.2021:
1. У классі Student додати можливість порівняння студентів за віком
2. У классі Student додати збереження списку всіх створених об'єктів
3. У классі Student додати альтернативну можливість створення нового об'єкту 
 зі словника


ДЗ від 25.09.2021:
1.  У классі Student додати перевірку, що в поле email неможливо записати щось, що не є валідною мейл адресою (валідна адреса - рядок, який обов'язково містить символ "@" , але не на першій чи останній позиції
2.  Реалізувати класс Lesson, який буде зберігати в собі дані про відвідування студентом заняття та отриману оцінку для кожної дати



'''
import json
import csv

student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender']

#STUDENTS = []

TEST_STUDENTS = [
    ['Mary', 'D', 'mail@mail.com', '19', 'Huston', 'F'],
    ['John', 'S', 'new_mail@mail.com', '21', 'London', 'M'],
    ['Andy', 'H', 'more_mail@mail.com', 'sexteen', 'Brighton', 'M']
]


class Student:

    ALL_STUDENTS = []

    def __init__(self, first_name = 'Noname', last_name = 'Nonamovich', email = 'Nomail',
     age = 'Noage', address = 'Noadress', gender = 'Nogender'):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.address = address
        self.gender = gender
# \/эта строка помещает нашу новую ссылку self полученную __init__ на только что созданный экземпляр в список ALL_STUDENTS класса Student
        Student.ALL_STUDENTS.append(self) 

#        self.inner_list = [self.first_name, self.last_name, self.email, self.age, self.address, self.gender]


    def __str__(self):
        return self.first_name.capitalize()

    @classmethod
    def from_dict(cls, dict_arg):
        obj = cls()
        index = 0
        for field in student_fields:
            setattr(obj, field, dict_arg[field])
        return obj

    
    @classmethod
    def add_student(cls):
        ''' function that adds a new student to list STUDENTS as dictionary '''
        temp_stud = []
        for field in range(len(student_fields)):
            temp_stud.append( input('Enter {}\t'.format(student_fields[field])) )
#      self.new_stud_ex = Student(*temp_stud)
        Student.ALL_STUDENTS.append(Student(*temp_stud))

    @classmethod
    def load_students(cls):
        for test_student in TEST_STUDENTS:
            print(test_student)
            Student(*test_student)
#            Student.ALL_STUDENTS.append(Student(*test_student))

#            self.new_stud_ex = Student(*test_student)
#            self.students_list.append(self.new_stud_ex)


#    def add_student(self):
#        ''' function that adds a new student to list STUDENTS as dictionary '''
#        temp_stud = []
#        for field in range(len(student_fields)):
#            temp_stud.append( input('Enter {}\t'.format(student_fields[field])) )
#
#        self.new_stud_ex = Student(*temp_stud)
#        self.students_list.append(self.new_stud_ex)


    @classmethod
    def print_students(cls):
        for student in cls.ALL_STUDENTS:
            print(student, " - is a student")
#            print(student.inner_list)
            # здесь можно и перебором через student.inner_list, но пока что так, 1-1
            print(' '.join(student_fields[0].capitalize().split('_')),":", '\t', student.first_name) 
            print(' '.join(student_fields[1].capitalize().split('_')),":", '\t', student.last_name)
            print(' '.join(student_fields[2].capitalize().split('_')),":", '\t', student.email)
            print(' '.join(student_fields[3].capitalize().split('_')),":", '\t', student.age)
            print(' '.join(student_fields[4].capitalize().split('_')),":", '\t', student.address)
            print(' '.join(student_fields[5].capitalize().split('_')),":", '\t', student.gender)
            print()        

         



    def __lt__(self, other): # lass than
        return self.age < other.age

    def __le__(self, other): # lass equal
        return self.age <= other.age

    def __eq__(self, other): # equal
        return self.age == other.age

    def __ne__(self, other): # not equal
        return self.age != other.age

    def __gt__(self, other): # greater than
        return self.age > other.age

    def __ge__(self, other): # gteater equal
        return self.age >= other.age




    '''    
    def print_student(self):
        print(self.first_name, self.last_name, self.email, self.age, self.address, self.gender)
    '''

#####################################/\class Student

class Student_list:
#    stud_list = []
    def __init__(self, students_list):
        if type(students_list) == list:
            self.students_list = students_list
        else:
            self.students_list = []

    def add_stud_to_list(self, student_inst):
        self.students_list.append(student_inst)

# OLD
    '''
    def add_student(self, new_student):
        if type(new_student) == list:
            self.new_stud_ex = Student(*new_student)
            self.students_list.append(self.new_stud_ex)
        else:
            print("it is not list type!")
    '''

# MOVED to class Student
    def add_student(self):
        ''' function that adds a new student to list STUDENTS as dictionary '''
        temp_stud = []
        for field in range(len(student_fields)):
            temp_stud.append( input('Enter {}\t'.format(student_fields[field])) )

        self.new_stud_ex = Student(*temp_stud)
        self.students_list.append(self.new_stud_ex)


# MOVED to class Student
    def print_students(self):
        for student in self.students_list:
            print(student, " - is a student")
#            print(student.inner_list)
            # здесь можно и перебором через student.inner_list, но пока что так, 1-1
            print(' '.join(student_fields[0].capitalize().split('_')),":", '\t', student.first_name) 
            print(' '.join(student_fields[1].capitalize().split('_')),":", '\t', student.last_name)
            print(' '.join(student_fields[2].capitalize().split('_')),":", '\t', student.email)
            print(' '.join(student_fields[3].capitalize().split('_')),":", '\t', student.age)
            print(' '.join(student_fields[4].capitalize().split('_')),":", '\t', student.address)
            print(' '.join(student_fields[5].capitalize().split('_')),":", '\t', student.gender)
            print()



# MOVED to class Student 
    def load_students(self):
        for test_student in TEST_STUDENTS:
            self.new_stud_ex = Student(*test_student)
            self.students_list.append(self.new_stud_ex)


    def dump_json(self):
        ''' function that save all students as dict into file JSON stored/created in "data" folder  '''
        with open('data\\student_data.json', 'w') as file:
            temp_stud = []
            for student in self.students_list:
                temp_stud.append(student.inner_list) 
            json.dump(temp_stud, file)


    def load_json(self, file_path='data\\student_data.json'):
        ''' function that load all students as dict from file JSON stored in "data" folder '''
        with open(file_path, 'r') as read_file:
#            temp_stud = []
#            self.students_list.extend(json.load(read_file))
#            temp_stud.append(json.load(read_file))
            temp_stud = (json.load(read_file))
            print(temp_stud)
            for student in temp_stud:
                self.new_stud_ex = Student(*student)
                self.students_list.append(self.new_stud_ex)
            



    def call_stud_list(self):
        return students_list        

#######################################################################/\class Student_list

class Group:
    def __init__(self, group_name, stud_list):
        self.group_name = group_name
        self.stud_list = stud_list

#not work   
def calculate_avg_age():

    try:
        total_age = 0
        for student in STUDENTS:
            total_age += int(student['age'])
        avgerage_age = total_age / len(STUDENTS)
        print('Average age is {}'.format(avgerage_age))
    except ValueError:
        print('Cannot calculate average age')
    except Exception as e:
        print(str(e))


#######################################################################/\class Group


# not work
def dump_csv():
    ''' function that save all students as dict into file CSV stored/created in "data" folder  '''
    with open('data\\student_data.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=student_fields)
        writer.writeheader()
        for student in STUDENTS:
            writer.writerow(student)

"""
# OLD
def load_json(file_path='data\\student_data.json'):
    ''' function that load all students as dict from file JSON stored in "data" folder '''
    with open(file_path, 'r') as read_file:
        STUDENTS.extend(json.load(read_file))
"""



# 2.2. закінчити функцію, яка виконує
# завантаження даних з файлу у форматі CSV.

# not work
def load_csv(file_path='data\\student_data.csv'):
    ''' function that load all students as dict from file CSV stored in "data" folder '''
    with open(file_path, 'r') as read_file:
        reader = csv.DictReader(read_file)
        for row in reader:
            STUDENTS.append(row)


# пришлось это перенести над ACTIONS потому что раньше интерпретатор не видел global_student_class_list и выдавал сообщение
# NameError: name 'global_student_class_list' is not defined
# 
list_students = []
global_student_class_list = Student_list(list_students)


'''
ACTIONS = {
    'add': global_student_class_list.add_student,
    'avg_age': calculate_avg_age,
    'load': global_student_class_list.load_students,
    'print': global_student_class_list.print_students,
    'dump_json': global_student_class_list.dump_json,
    'dump_csv': dump_csv,
    'load_json': global_student_class_list.load_json,
    'load_csv': load_csv
}
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
#    list_students = []
#    global_student_class_list = Student_list(list_students)
#    ['first_name', 'last_name', 'email', 'age', 'address', 'gender']
    
    some_dict = {'first_name': 'Vasya', 'last_name': 'Pupkin', 'email': 'vasiliyp@mail.com', 'age': '23', 'address':'Gorishni Plavni', 'gender': 'M'}

    print('The lenght of ALL_STUDENTS list', len(Student.ALL_STUDENTS))
    vasya = Student.from_dict(some_dict)
#    global_student_class_list.add_stud_to_list(vasya)
#    global_student_class_list.print_students()
    print()
#    print(global_student_class_list.students_list[0])
#    print(global_student_class_list.students_list[0].inner_list)
#    Student.ALL_STUDENTS.append(self)
    print()
    print('The lenght of ALL_STUDENTS list', len(Student.ALL_STUDENTS))
    print(Student.ALL_STUDENTS[0])
    print(Student.ALL_STUDENTS[0].last_name)



    '''

    global_student_class_list.load_students()

    print(global_student_class_list.students_list[0])
    print(global_student_class_list.students_list[0].age)

    print(global_student_class_list.students_list[1])
    print(global_student_class_list.students_list[1].age)

    print(global_student_class_list.students_list[0]<global_student_class_list.students_list[1])
    print(global_student_class_list.students_list[0]>global_student_class_list.students_list[1])
    '''

#    global_student_class_list.load_json()
  
#    global_student_class_list.print_students()

#    global_student_class_list.dump_json()

    while True:
        action = input('Desired action:\t')
        if action in ACTIONS:
            print('The lenght of ALL_STUDENTS list', len(Student.ALL_STUDENTS))
            ACTIONS.get(action)()
        else:
            break

'''
ACTIONS = {
    'add': add_student,
    'avg_age': calculate_avg_age,
    'load': load_students,
    'print': global_student_class_list.print_students,
    'dump': dump_studens,
    'dump_csv': dump_csv,
    'load_json': load_from_json,
    'load_csv': load_csv
}

'''
