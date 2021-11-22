'''
#1
ДЗ від 11.09.2021
У поточному проекті у файлі students.py :
1. Змінити функцію print_student(student) так, щоб вона виводила назви полів у людино-читаємому вигляді: кожне з великої літери, з пробілами замість "_"
2. Написати функцію print_students_list() , яка виводитиме весь список студентів (викликатиме у циклі print_student(student)
 для кожного студента та візуально відокремлюватиме вивід інформації про кожного зі студентів)
3. Результат виконання залити у свій проект на гітхабі
У LMS:
 переглянути матеріали до заняття № 10 (контестні менеджери та файли), пройти тести
Додатково:
 подивится на CSV файли , модуль у python для роботи з csv .

Мій проект на гітхабі: https://github.com/jane-at-beetroot/basics

# 2
ДЗ від 13.09.2021:
1. у файлі lms.students.py змінити шляхи до файлів у всіх функціях так, щоб файли потрапляли не в кореневу папку проекту, а в папку lms/data.
2. закінчити функцію, яка виконує завантаження даних з файлу у форматі CSV.
3. у файлі lms/data/exam.json описати ще 4 питання по основам Python з трьому варінатами відповідей кожне (правильна відповідь для кожного питання тільки одна).
4. подивитися теоретичний матеріал щодо класів у Beetroot LMS
'''
import json
import csv


student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender']

STUDENTS = []

TEST_STUDENTS = [
    ['Mary', 'D', 'mail@mail.com', '19', 'Huston', 'F'],
    ['John', 'S', 'new_mail@mail.com', '21', 'London', 'M'],
    ['Andy', 'H', 'more_mail@mail.com', 'sexteen', 'Brighton', 'M']
]

def add_student():
    student = {}
    for field in student_fields:
        student[field] = input('Enter {}\t'.format(field))
        if field == 'age':
            try:
                int(student['age'])
            except:
                student['age'] = input('Enter age as number\t')
    STUDENTS.append(student)
   
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

''' 
1.1. Змінити функцію print_student(student) так,
 щоб вона виводила назви полів у людино-читаємому вигляді:
  кожне з великої літери, з пробілами замість "_"

'''
def print_student(student):
    for field in student:
        print(' '.join(field.capitalize().split('_')),":", '\t', student[field])
    print('\n')

''' 
1.2. Написати функцію print_students_list() , 
яка виводитиме весь список студентів 
(викликатиме у циклі print_student(student)
 для кожного студента та візуально відокремлюватиме
 вивід інформації про кожного зі студентів)
 '''
def print_students_list():
    '''Call print_student() for every student in STUDENTS'''
    for student in STUDENTS:
            print_student(student)

def load_students():
    for test_student in TEST_STUDENTS:
        STUDENTS.append(dict(zip(student_fields, test_student)))
#    print(STUDENTS)


def load_students():
    for test_student in TEST_STUDENTS:
        STUDENTS.append(dict(zip(student_fields, test_student)))

def dump_studens():
    with open('data\\student_data.json', 'w') as file:
        json.dump(STUDENTS, file)

def dump_csv():
    with open('data\\student_data.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=student_fields)
        writer.writeheader()
        for student in STUDENTS:
            writer.writerow(student)

''' 2.2. закінчити функцію, яка виконує
 завантаження даних з файлу у форматі CSV.
 '''

def load_csv(file_path='data\\student_data.csv'):
    with open(file_path, 'r') as read_file:
        reader = csv.DictReader(read_file)
        for row in reader:
            STUDENTS.append(row)

def load_from_json(file_path='data\\student_data.json'):
    with open(file_path, 'r') as read_file:
        STUDENTS.extend(json.load(read_file))


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

if __name__ == '__main__':

    while True:
        action = input('Desired action:\t')
        if action in ACTIONS:
            ACTIONS.get(action)()
        else:
            break

