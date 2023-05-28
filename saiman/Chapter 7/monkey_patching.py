class Student:
    def __init__(self,name):
        self.name=name




m1=Student("saiman")

Student.roll=20
print(Student.roll)
print(m1.name)

def display_name(self):
    print(self.name)

def display_roll(self):
    print(self.roll)

Student.display_name = display_name
Student.display_roll = display_roll

m1.display_name()
m1.display_roll()

s2=Student('Himal')
s2.roll=50
print(s2.roll,m1.roll)



