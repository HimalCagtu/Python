# Building blocks of an OOP
#
# An object-oriented programming contains different elements which are as follows:
#
#     Classes: Classes are user-defined data types that acts as a blueprint for individual objects.
#     Objects: Objects are instances of a class that contains specific data. Generally objects can represent real-world objects such as human, room, etc.
#     Methods: Methods are functions that are bound to specific objects. For example, a human object can have talk method, whereas a computer object can have boot method.
#     Attributes: Attributes are variables that define the property of an object Attributes can also be defined as a state of an object for example, if we create an object for a rectangle, then length and width will be attributes for it.

#
# class Person:
#     species = 'Human'
#
#     def __init__(self, first_name, last_name):
#         print("Hello I am initialized")
#         self.first_name = first_name
#         self.last_name = last_name
#         print(f'{self.first_name}   {self.last_name}')
#
#     def full_name(self):
#         return f'Your name is {self.first_name} {self.last_name}'
#
#
# person_1 = Person('Himal', 'Subedi')
#
# print(person_1.first_name)


# class DomesticAnimal:
#     category = 'Dog'
#
#     def __init__(self, name, sound):
#         self.name = name
#
#         self.sound = sound
#         print("The dog is {} and the sound is {}".format(name, sound))
#
#
# inp = input("Enter the dog name to get sound").lower()
# if inp == 'cocker':
#     dog1 = DomesticAnimal('cocker', "Bhau bhau")
# elif inp == 'german':
#     dog1 = DomesticAnimal('German', 'Bhau bhau')
# elif inp == 'husky':
#     dog1 = DomesticAnimal('husky', 'Bhau bhau')
# else:
#     print("Dog not in database")

class Person:

    def __init__(self,first_name,last_name,age):

        self.fname=first_name
        self.lname=last_name
        self.age=age
        print(f'The name is {self.fname} {last_name} and age is {age}')

    def __str__(self):
        return self.fname,self.lname,self.age

    def lang(self):
        return f'{self.fname}  {self.lname} speaks Nepali langauge '






Himal=Person("himal",'subedi',20)
print(Himal.__str__())
print(Himal.__dict__)
print(Himal.__sizeof__())

print(Himal.lang())


































