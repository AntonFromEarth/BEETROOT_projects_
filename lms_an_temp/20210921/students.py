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

    def __init__(self, first_name, last_name, email, age, address, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.address = address
        self.gender = gender
        self.inner_list = [self.first_name, self.last_name, self.email, self.age, self.address, self.gender]

    def __str__(self):
        return self.first_name.capitalize()
    '''    
    def print_student(self):
        print(self.first_name, self.last_name, self.email, self.age, self.address, self.gender)
    '''


class Student_list:
#    stud_list = []
    def __init__(self, students_list):
        if type(students_list) == list:
            self.students_list = students_list
        else:
            self.students_list = []

# OLD
    '''
    def add_student(self, new_student):
        if type(new_student) == list:
            self.new_stud_ex = Student(*new_student)
            self.students_list.append(self.new_stud_ex)
        else:
            print("it is not list type!")
    '''

# NEW
    def add_student(self):
        ''' function that adds a new student to list STUDENTS as dictionary '''
        temp_stud = []
        for field in range(len(student_fields)):
            temp_stud.append( input('Enter {}\t'.format(student_fields[field])) )
            if field == 'age':
                try:
                    int(student['age'])
                except:
                    student['age'] = input('Enter age as number\t')
#        students_list.add_student(temp_stud)
        self.new_stud_ex = Student(*temp_stud)
        self.students_list.append(self.new_stud_ex)


    #NEW!!!
    def print_students(self):
        for student in self.students_list:
            print(student, " - is a student")
            print(student.inner_list)
            print(' '.join(student_fields[0].capitalize().split('_')),":", '\t', student.first_name) 
            print(' '.join(student_fields[1].capitalize().split('_')),":", '\t', student.last_name)
            print(' '.join(student_fields[2].capitalize().split('_')),":", '\t', student.email)
            print(' '.join(student_fields[3].capitalize().split('_')),":", '\t', student.age)
            print(' '.join(student_fields[4].capitalize().split('_')),":", '\t', student.address)
            print(' '.join(student_fields[5].capitalize().split('_')),":", '\t', student.gender)
            print()



# NEW
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


class Group:
    def __init__(self, group_name, stud_list):
        self.group_name = group_name
        self.stud_list = stud_list

   
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

def load_csv(file_path='data\\student_data.csv'):
    ''' function that load all students as dict from file CSV stored in "data" folder '''
    with open(file_path, 'r') as read_file:
        reader = csv.DictReader(read_file)
        for row in reader:
            STUDENTS.append(row)




'''
# OLD
ACTIONS = {
    'add': add_student,
    'avg_age': calculate_avg_age,
    'load': load_students,
    'print': print_students_list,
    'dump': dump_studens,
    'dump_csv': dump_csv,
    'load_json': load_from_json,
    'load_csv': load_csv
}
'''

# пришлось это перенести над ACTIONS потому что раньше интерпретатор не видел global_student_class_list и выдавал сообщение
# NameError: name 'global_student_class_list' is not defined
# 
list_students = []
global_student_class_list = Student_list(list_students)

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


if __name__ == '__main__':
#    list_students = []
#    global_student_class_list = Student_list(list_students)


#    global_student_class_list.load_students()

#    global_student_class_list.load_json()
  
#    global_student_class_list.print_students()

#    global_student_class_list.dump_json()

    while True:
        action = input('Desired action:\t')
        if action in ACTIONS:
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