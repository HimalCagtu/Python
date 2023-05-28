# Encapsulation is the process of restricting the
# direct access to the data.
# It can be achieved by binding the private attribute along with methods to make the data usable.
# In python we make the data protected by naming the attributes and methods starting with
# single underscore_ or double underscores __.
# The methods that are bound with protected attributes are called as getters and setters.
# the getter method takes no arguments and setter takes one argument except self.

# class Person:
#  _name='Saiman'
#
#  bge=22
#
#  def age(self):
#      return self._name,self.bge
#
#  def set_age(self,age):
#      self.bge=age
#      return self.bge
#
#
#
#
#
#
# p1=Person()
# print(p1.age())
#
# print(p1.set_age(30))
# print(p1._name)
#

# class Student:
#
#     is_large=False
#
#     def __init__(self,name,roll):
#
#         self.name=name
#         self.roll=roll
#
#
#
#
#
#     def add_student(self):
#         self.lst.append(Student)
#
#
#         if len(self.lst)>2:
#             self.is_large=True
#             print(self.is_large)
#         # else:
#         #     print("false")
#
#
#
#
# s1=Student('Himal',11)
# s1.add_student()
# s2=Student('Saiman',12)
# s2.add_student()
# s3=Student('suraj',13)
# s3.add_student()
# print(len(s1.lst))


# The @property decorator
#
#     They look like regular object variables but are capable of attaching custom behavior to the class.
#     They are used as better alternative of getters and setters
#     whenever we create a property inside a class, it's behavior will be tightly controlled.
#
# Why do we use @property instead of getters and setters?
#
#     Property decorators make the function behave like an attribute so that we can just use an assignment operator instead of calling a method to access or set values of the variable.
#     It makes the code look much cleaner than using getters and setters.
#


#
# class Student:
#     def __init__(self,name,rolll):
#         self.name=name
#         self.roll=rolll
#
#     @property
#     def get_name(self):
#         return self.name
#
#     @get_name.setter
#     def get_name(self,name):
#         self.name=name
#         return self.name
#
#     @get_name.deleter
#     def get_name(self):
#         self.name=''
#
#
#
# s1=Student("himal",22)
# print(s1.get_name)
# s1.get_name=('Wagle')
# print(s1.get_name)
#
# del s1.get_name
# print(s1.get_name)


class MyClass:
    _value = -1

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value


mc = MyClass()
print(mc.get_value())
mc.set_value(46)
print(mc.get_value())

MALE = 'male'
FEMALE = 'female'


class Student:
    def __init__(self, name, roll, gender):
        self.name = name
        self.gender = gender
        self.roll = roll


class ClassRoom:
    def __init__(self, name, class_teacher):
        self.students = []
        self.is_large = False

        self.name = name
        self.class_teacher = class_teacher

    def add_students(self,student:Student):
        print("[ADDING STUDENT]".center(80,'='))
        self.students.append(student)
        print(f'{student.name} sucessfully added')
        if len(self.students)>3:
            self.is_large=True
            print(self.is_large)

    def remove_students(self,student:Student):
        print("[REMOVING STUDENT".center(80,'*'))
        if student in self.students:
            self.students.remove(student)
            print(f'{student.name} sucessfully removed')
            if len(self.students)>3:
                self.is_large=True


        else:
            print(f'{student.name} does not exist')






c1=ClassRoom('Python',"Sudip Ghimire")
s1=Student('Saiman Khatiwada',1,MALE)
c1.add_students(s1)
s2=Student('Suraj Rajbanshi',2,MALE)
c1.add_students(s2)
s3=Student('Himal Subedi',3,MALE)
c1.add_students(s3)

c1.remove_students(s1)

