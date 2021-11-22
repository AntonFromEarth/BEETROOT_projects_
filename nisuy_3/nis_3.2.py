import json
class C:
    my_list = []
    task_list = []
    def __init__(self, name = None):
        self.id = len(C.my_list)+1
        self.x = name
        self.y = None
        C.my_list.append(self)

    def __str__(self):
        return "{}".format(self.id)

    def __repr__(self):
        return "The id is: {}".format(self.id)

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def list_to_json(cls):
        task_list = [t.__dict__ for t in cls.my_list]
        print("my_list = ", C.my_list)
        print("task_list = ", task_list)
        return json.dumps(task_list)
        #return C.task_list

    @property
    def x(self):
        """I'm the 'x' property."""
        print("in getter")
        return self._x

    @x.setter
    def x(self, value):
        print("in setter")
        self._x = value

    #@x.deleter
    #def x(self):
        #del self._x

#c=C('Hu')
c_1=C(1.1)
c_2=C(2.2)
c_3=C(3.3)
print('c_1.x_1 = ',c_1.x)
print("c_1 = ", c_1)
#print('c_1.x_1 = ',c_1._x)
#print('c_1.x_1 going to change')
#c_1.x = 5
print()
#print('c_1.x_2 = ',c_1.x)
#print('c_1.x_2 = ',c_1._x)
c_1.y = "Hi!"
print()
print("c_1.__dict__ = ", c_1.__dict__)
print()
print("by getattr = ",getattr(c_1, 'x'))
print()

print("C.my_list = ", C.my_list)
print()
#print("C.__dict__ = ", C.__dict__)
print("c_1.to_json = ", c_1.to_json)
print()
print("C.list_to_json = ", C.list_to_json())
print()
print("C.task_list = ",C.task_list)

