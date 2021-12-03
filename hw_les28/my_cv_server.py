
"""
3. За допомогою фреймворку Flask реалізувати простий сервер
, який буде мати два url:
    - "/" - повертає список повних імен всіх персон (first_name + last_name)
    , у текстовому представленні.
    - "/person/<int:person_id>" - повертає текcтове представлення
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



"""
#######  GOOD  #############
from flask import Flask

from flask import Blueprint, request

#from .models import Task
#from les28_cv_build import Person, some
import les28_cv_build as les

#app = Flask('task', __name__)
app = Flask(__name__)

@app.route("/")
def person_list():
    obj = les.Person()
    obj2 = les.Person.load_from_json()

    #return "Hi!"
    #return obj.Person.to_json()
    #return les.Person.persons
    #return les.some
    return obj2.to_json()
    #return "<p>Hello, Vasya!</p>"

####### /GOOD /#############
"""


### 
# (?) почему то не работает в файле __init__.py
from flask import Flask
import json


def create_app():
    app = Flask(__name__)

    from . import my_cv_server
    #app.register_blueprint(my_cv_server.bp)
    app.register_blueprint(my_cv_server.bp)

    return app
###

from flask import Blueprint, request
from .les28_cv_build import Person, some, some2

#bp = Blueprint('person', __name__) #Y.T.L23 (23.11.2021) 2:49:02
bp = Blueprint('my_cv_server', __name__)

'''
Blueprint (обстракция, схема) позволяет нам создать общую схему ветки
 роутов (как это сделано внизу) и уже потом всю эту схему добавить к аппликэйшену
 Тоесть мы не добавляем в апликацию наши роуты по отдельности, а добавляем
 сразу целое дерево. И нам не нужно импертировать переменную app в середину этого
  файла
Сам блупринт импортируется в файле __init__.py

'''

###
# из сайта Фласк: декоратор route () используется, чтобы сообщить Flask, какой URL-адрес должен запускать нашу функцию.
@bp.route('/', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST': #Y.T.L23 (23.11.2021) 3:04:14 если пришел запрос POST 
        data = request.get_json(force=True) #Y.T.L23 (23.11.2021) 3:04:55 - вытягивание необходимых нам данных для создания новой задачи
        #new_task = Task(**data) #Y.T.L23 (23.11.2021) 3:05:05 создание нового объекта задачи из данных data полученных выше и передача их в констректор Task и сохранение под именем new_task
        new_task = Person(**data)
        return new_task.to_json()#Y.T.L23 (23.11.2021) 3:05:18 и возвращение ДЖЕСОН представление этой одной задачи new_task
#    return Task.list_to_json() #Y.T.L23 (23.11.2021) 3:03:33, если от браузера пришел запрос GET - возвращаем список всех своих задач в виде json
    
    #new_person = Person("Vasya", "Pupkin") # MY CHECK
    #return "<p>Hello, Vasya!</p>" # MY CHECK
    return Person.persons_list_to_json()

'''
Y.T.L23 (23.11.2021) 3:05:32 - браузер умеет делать только GET запросы,
 а что бы что то отправлять на нашь сервер POST-запрос, будем использовать командную строку (консоль)
'''
@bp.route('/<int:person_id>')
def person_detail(person_id):
    for person in Person.persons:
        print("person in person_detail = ", person)
        if person.id == person_id:
            return json.dumps(str(person))

    return "No that person"

###