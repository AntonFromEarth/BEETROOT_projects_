
some = "Hello Flask!"
some2 = {"asder":"afsd"}
"""
Загальна мета заняття - розробити основні елементи сайта,
 що надає сервіс конструктора резюме для користувачів. 
 Ідея полягає в тому, що користувач може додати свій обліковий запис,
 додавати/змінювати/видаляти контакти, навички та досвід роботи,
 а система згенерує сторінку з його резюме.

Для реалізації задуму треба:
1. Реалізвуати класи, які будуть виконувати роль моделей даних.

    - class Skill - описує одну за навичок користувача.
     Навички можуть бути трьох категорій (category):
    технології (technologies), методолії (methodologies)
    та мови (languages). Кожна навичка характеризується
    такими параметрами: 
    назва (name),
    досвід (experience) - кількість років використання
    цієї технології/методолгії/мови,
    рівень володіння навичкою (level) - вибір з
    п'яти можливих варіантів:
    beginner, 
    junior, 
    middle, 
    senior, 
    expert.

    - class Contact - описує контактні дані користувача.
     Описується полями тип (contact_type) - вибір з
      варіантів 'phone' та 'email'; та значення (value) -
       конкретна мейл-адреса або номер телефону користувача.

    - class JobExperience - описує доствід роботи користувача.
     Харкатеризується атрибутами: 
     дата початку роботи (start_date), 
     дата завершення роботи (end_date), 
     компанія (company), 
     посада (position).

    - class Person - описує особу самого користувача. 
    Має атрибути  ім'я (first_name), 
    прізвище (last_name), 
    дата народження (birth_date), 
    а також списки контактів (об'єкти класу Contact), 
    навичок (об'єкти класу Skill) 
    та досвіду роботи (об'єкти класу JobExperience). 
    Кожен об'єкт класу має також атрибут id - 
    унікальний ідентифікатор користувача в системі.


2. Реалізувати відповідні методи для класу Person:
 2.1 - Для кожного зі списків (контакти, навички, досвід роботи) 
    мають бути реалізовані 
    2.1.1 (-) - методи додавання (add), 
    2.1.2 (-) - видалення (delete) та 
    2.1.3 (-) - оновлення (update) елементів списку.
     Для реалізації цих методів можливо буде
      необхідне додавання вспоміжних атрибутів для кожного
       класу.

 2.2(+) - Реалізвуати методи (2.2.1)(+)збереження інфомації про об'єкт
     класу Person разом з усіма вкладеними об'єктами
     у JSON файл (2.2.2)(+)та завантаження JSON файлу
      із створенням всіх вкладених об'єктів.

 2.3(-) - Реалізувати метод, який представляє список skills
     персони, розбитий за категоріями.
     Метод має повертати словник, де ключами є категорії
      навичок, а значеннями - списки об'єктів навичок персони,
      що належать до цієї категорії, відсортовані 
      за зменшенням досвіду
       (навичка з найбільшим значенням досвіду 
       у цій категорії йде перша).

 2.4(-) - Реалізувати метод, який сортує досвід роботи персони
     від найбільш актуального
     до найбільш давнього (останній досвід роботи йде першим
      у відсортованому списку, найбільш давній - останнім)


3. За допомогою фреймворку Flask реалізувати простий сервер
, який буде мати два url:
 3.1 (+) - "/" - повертає список повних імен всіх персон (first_name + last_name)
    , у текстовому представленні.
 3.2 (+) - "/person/<int:person_id>" - повертає тектове представлення
     інформації про одного користувача.

За необхідності можна додавати будь-які службові атрибути та методи для будь-яких класів.
 Усе рішення має міститися в окремій папці з назвою cv_builder.

ДЗ від 10.11.2021:
4. До серверу із попереднього завдання додати можлисіть створення 
 (POST "/") та оновлення користувачів (PATCH "/<id>"). 
 Інформація у обох запитах має бути струткрована як JSON.
  Методи для обробки запитів у Flask:
   https://flask.palletsprojects.com/en/2.0.x/api/#incoming-request-data.
    Для тестування розробленого функціоналу використати бібліотеку
     requests, за допомогою якої можна надсилати потрібні
      запити до розроблюваного серверу.
"""
import os
import json


class Skill:
    categories = ['technologies', 'methodologies', 'languages']
    levels = ['beginner', 'junior', 'middle', 'senior', 'expert']

    def __init__(self,category = None, name = None, experience = None, level = None):
        self.category = category
        self.name = name
        self.experience = experience
        self.level = level
        
    def __str__(self):
        return "{} {}".format(self.category, self.name)

    def __repr__(self):
        return "The skill: {}".format(self.category)
        
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value in self.categories:
            self._category = value
        elif value == None:
            self._category = value
        else:
            raise ValueError('Category value is out of range')

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, val):
        if val in self.levels:
            self._level = val
        elif val == None:
            self._level = val
        else:
            raise ValueError('Level value is out of range')

    @classmethod
    def create_inst_from_dict(cls, user_dict):
        new_inst = Skill()
        for key, value in user_dict.items():
            setattr(new_inst, key, value)
        return new_inst

class Contact:

    contact_types = ['email', 'phone']
    def __init__(self, contact=None, value=None):
        self.contact = contact
        self.value = value

    def __str__(self):
        return "{} (str)".format(self.contact)

    def __repr__(self):
        return "The contact: {} (repr)".format(self.contact)

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, cont):
        if cont in self.contact_types:
            self._contact = cont
        elif cont == None:
            self._contact = None
        else:
            raise ValueError('Contact value is out of range')

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if self.contact == self.contact_types[0]:
            self._value = val
        elif self.contact == self.contact_types[1]:
            self._value = val
        elif val == None:
            self._value = None
        else:
            raise ValueError('Value of value is out of range')

    @classmethod
    def create_inst_from_dict(cls, user_dict):
        new_inst = Contact()
        for key, value in user_dict.items():
            setattr(new_inst, key, value)
        return new_inst


class JobExperience:

    def __init__(self, start_date=None, end_date=None, company=None, position=None):
        self.start_date = start_date
        self.end_date = end_date
        self.company = company
        self.position = position

    def __str__(self):
        return "Job exp. in company(str) {}".format(self.company)

    def __repr__(self):
        return "The position (repr): {}".format(self.position)

    @classmethod
    def create_inst_from_dict(cls, user_dict):
        new_inst = JobExperience()
        for key, value in user_dict.items():
            setattr(new_inst, key, value)
        return new_inst


'''
- (+) class Person - описує особу самого користувача. 
Має атрибути  ім'я (first_name), 
прізвище (last_name), 
дата народження (birth_date), 
а також списки контактів (об'єкти класу Contact), 
навичок (об'єкти класу Skill) 
та досвіду роботи (об'єкти класу JobExperience). 
Кожен об'єкт класу має також атрибут id - 
унікальний ідентифікатор користувача в системі.

2. Реалізувати відповідні методи для класу Person:
    - Для кожного зі списків (контакти, навички, досвід роботи) 
    мають бути реалізовані 
    методи додавання (add), видалення (delete) та 
    оновлення (update) елементів списку.
     Для реалізації цих методів можливо буде
      необхідне додавання вспоміжних атрибутів для кожного
       класу.

    - Реалізвуати методи збереження інфомації про об'єкт
     класу Person разом з усіма вкладеними об'єктами
     у JSON файл та завантаження JSON файлу
      із створенням всіх вкладених об'єктів.

    - Реалізувати метод, який представляє список skills
     персони, розбитий за категоріями.
     Метод має повертати словник, де ключами є категорії
      навичок, а значеннями - списки об'єктів навичок персони,
      що належать до цієї категорії, відсортовані 
      за зменшенням досвіду
       (навичка з найбільшим значенням досвіду 
       у цій категорії йде перша).

    - Реалізувати метод, який сортує досвід роботи персони
     від найбільш актуального
     до найбільш давнього (останній досвід роботи йде першим
      у відсортованому списку, найбільш давній - останнім)

'''


# Этот класс отвечает за создание основной характеристики клиента
# и включает в себя списки из экземпляров сверху описанных классов
# В этом классе должны быть прописаны атрибуты сохранаяющие все данные
# клиента в файл в формате ДЖЕСОН, создающий клиента из существующего файла ДЖЕСОН
class Person:
    persons = []
    def __init__(self, first_name=None, last_name = None, birth_date = None):
        self.id = len(Person.persons) + 1
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.contacts = []
        self.skills = []
        self.job_experiences = []
        Person.persons.append(self)

    def __str__(self):
        return "{} {} (str)".format(self.first_name, self.last_name)

    def __repr__(self):
        return "Person - {} {} (repr)".format(self.last_name, self.first_name)



    # метод добавляющий контакт в список контактов экземпляра класса Person почленным способом
    def add_contact(self, contact_arg, value_arg):
        self.contacts.append(Contact(contact_arg, value_arg))

    def add_skill(self, category, name, experience, level):
        self.skills.append(Skill(category, name, experience, level))

    def add_job_experience(self, start_date, end_date, company, position):
        self.job_experiences.append(JobExperience(start_date, end_date, company, position))

    # метод изменяющий уже существующий контакт в списоке контактов экземпляра класса Person почленным способом
    def update_contact(self, new_contact_arg, new_value_arg, upd_val_arg):
        #print('In update contact', new_contact_arg, new_value_arg, upd_val_arg) # MY CHECK
        if self.contacts:
            for contact in self.contacts:
                #print('contact = ', contact) # MY CHECK
                #print('contact.contact = ', contact.contact) # MY CHECK
                if contact.contact == upd_val_arg:
                    #print('contact.contact = ', contact.contact) # MY CHECK
                    contact.contact = new_contact_arg
                    contact.value = new_value_arg
                    #print('contact.value = ', contact.value) # MY CHECK

    def update_skill(self, change_in_category, new_name, new_experience, new_level):
        if self.skills:
            for skill in self.skills:
                if skill.category == change_in_category:
                    skill.name = new_name
                    skill.experience = new_experience
                    if new_level in Skill.levels:
                        skill.level = new_level

    def update_job_experience(self, new_start_date, new_end_date, upd_company, new_position):
        if self.job_experiences:
            for job_experience in self.job_experiences:
                if job_experience.company == upd_company:
                    job_experience.start_date = new_start_date
                    job_experience.end_date = new_end_date
                    job_experience.position = new_position


    def del_contact(self,contact_for_del):
        if self.contacts:
            for contact in self.contacts:
                if contact.contact == contact_for_del:
                    del self.contacts[self.contacts.index(contact)]

    def del_skill(self, skill_category_for_del):
        if self.skills:
            for skill in self.skills:
                if skill.category == skill_category_for_del:
                    del self.skills[self.skills.index(skill)]


    def del_job_experience(self,exp_company_for_del):
        if self.job_experiences:
            for job_experience in self.job_experiences:
                if job_experience.company == exp_company_for_del:
                    del self.job_experiences[self.job_experiences.index(job_experience)]





    # Этот метод создает и возвращает новый экземпляр класса но с полученного внешнего словаря.
    # Он запускает в своем теле подобные методы из других внешних классов котороые соствляют его соответствующие списки 
    @classmethod
    def create_inst_from_dict(cls, user_dict):
        new_inst = Person()
        for key, value in user_dict.items():
            if key == 'contacts':
                for index in user_dict[key]:
                    new_inst.contacts.append(Contact.create_inst_from_dict(index))
                continue

            elif key == 'skills':
                for index in user_dict[key]:
                    new_inst.skills.append(Skill.create_inst_from_dict(index))
                continue

            elif key == 'job_experiences':
                for index in user_dict[key]:
                    new_inst.job_experiences.append(JobExperience.create_inst_from_dict(index))
                continue

            setattr(new_inst, key, value)
        return new_inst


    # Этот метод превращает все что представляет из себя экземпляр класса в его магическом
    # словаре (self.__dict__) в JSON. 
    # Но важно превратить все элементы в магическом словаре в джесоно-читаемый формат.
    # Например, простой список экземпляров класса джесон не прочитает и выпадет ошибка. 
    # Для этого есть строка превращающая каждый экземпляр класса в строке, в словрью
    def to_json(self): 
        temp_dict = {}
        for key, value in self.__dict__.items(): # словарный вид экземпляра класса 
            if type(value) == list:
                temp_dict[key] = [t.__dict__ for t in value] # строка превращающая каждый экземпляр класса в строке, в словрь
                continue
            temp_dict[key] = value
        return json.dumps(temp_dict)

    # Метод сохраняющий все данные созданного экземпляра класса Персон в новый файл,
    # который он де и создает в формате JSON в папку (дирректорию) data 
    def dump_to_json(self):
        path_data = os.path.join(os.getcwd(), "data", "person_data.json")
        temp_dict = {}
        for key, value in self.__dict__.items():
            if type(value) == list:
                temp_dict[key] = [t.__dict__ for t in value]
                continue
            temp_dict[key] = value
        with open(path_data, 'w') as file:
            json.dump(temp_dict, file)

    # Метод открывающий файл в формате ДЖЕСОН с информацией клиента, копирует
    # всю информацию в формат словаря и передает в метод в самом классе
    # создающий новый экземпляр класса Персон, его же и возвращает.
    @classmethod
    def load_from_json(cls):
        path_data = os.path.join(os.getcwd(), "data", "person_data.json")
        with open(path_data, 'r') as file:
            out_dict_person = json.load(file)
        new_inst_of_Person = Person.create_inst_from_dict(out_dict_person)
        return new_inst_of_Person

    # 
    @classmethod
    def persons_list_to_json(cls):
        #persons_list = [p.__dict__ for p in cls.persons]
        persons_list = [str(p) for p in cls.persons]
        print('persons_list_to_json = ', persons_list) # MY CHECK

        return json.dumps(persons_list)

    """
     2.3(-) - Реалізувати метод, який представляє список skills
     персони, розбитий за категоріями.
     Метод має повертати словник, де ключами є категорії
      навичок, а значеннями - списки об'єктів навичок персони,
      що належать до цієї категорії, відсортовані 
      за зменшенням досвіду
       (навичка з найбільшим значенням досвіду 
       у цій категорії йде перша).
    """
    def skills_by_rating(self):
        pass

    """
    class Skill:
    categories = ['technologies', 'methodologies', 'languages']
    levels = ['beginner', 'junior', 'middle', 'senior', 'expert']

    def __init__(self,category = None, name = None, experience = None, level = None):
        self.category = category
        self.name = name
        self.experience = experience
        self.level = level
        
    def __str__(self):
        return "{} {}".format(self.category, self.name)

    def __repr__(self):
        return "The skill: {}".format(self.category)
        
    """

'''
user_person_dict = {"id": 1, "first_name": "Fiodor", "last_name": "Petrov", "birth_date": "11.11.1991", "contacts": [{"_contact": "email", "_value": "vasya@mail.com"}], "skills": [{"_category": "languages", "name": "C", "experience": 3, "_level": "beginner"}], "job_experiences": [{"start_date": "12.12.2015", "end_date": "10.10.2016", "company": "Roga i kopita", "position": "Cleaner"}]}
print("user_person_dict = ", user_person_dict)
print()
some_person_3 = Person.create_inst_from_dict(user_person_dict)
print("some_person_3.__dict__ = ", some_person_3.__dict__)
'''

some_person_3 = Person.load_from_json()
#print("some_person_3.__dict__ = ", some_person_3.__dict__)
#print("some_person_3.to_json() = ", some_person_3.to_json())
some_person_1 = Person()
#print(some_person_1.persons)
print(Person.persons_list_to_json())
print(str(some_person_1))
print(some_person_3.to_json())
print()
some_person_3.update_contact(new_contact_arg = 'email', new_value_arg = 'fiodorP@mail.com', upd_val_arg = 'email')
print('some_person_3 after update email:\n', some_person_3.to_json())

'''
person_id = 2
for person in Person.persons:
    if person.id == person_id:
        print('person = ', json.dumps(str(person)))
'''





"""
3. За допомогою фреймворку Flask реалізувати простий сервер
, який буде мати два url:
    - "/" - повертає список повних імен всіх персон (first_name + last_name)
    , у текстовому представленні.
    - "/person/<int:person_id>" - повертає тектове представлення
     інформації про одного користувача.

За необхідності можна додавати будь-які службові атрибути та методи для будь-яких класів.
 Усе рішення має міститися в окремій папці з назвою cv_builder.
"""



