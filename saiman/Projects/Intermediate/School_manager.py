import json


class Student:
    def __init__(self, first_name, last_name, roll, age, major):
        self.first_name = first_name
        self.last_name = last_name
        self.roll = roll
        self.age = age
        self.major = major

    def get_full_name(self):
        self.full_name = self.first_name + self.last_name
        return self.full_name

    def __str__(self):
        return self.full_name, self.roll


class Grade(Student):
    classes = []

    def __init__(self, name, first_name, last_name, roll, age, major):
        self.name = name
        super().__init__(first_name, last_name, roll, age, major)
        self.students = []

    def list_students(self):
        print('=' * 60)
        print(f'{self.name}')
        print('Roll'.rjust(5), 'Full Name'.ljust(40), 'Age'.rjust(3), 'Major'.ljust(20))
        for i in self.students:
            print(i.roll)

    def add_student(self):
        # first_name = input("Enter first name")
        # last_name = input("Enter last name")
        # age = input("Enter age")
        # roll = input("Enter roll")
        # major = input("Enter major")

        add = Student(
            first_name=input("Enter first name"),
            last_name=input("Enter last name"),
            age=int(input("Enter age")),
            roll=int(input("Enter roll")),
            major=input("Enter major")
        )
        self.students.append(add)
        data = {'name': self.name, 'students': [i.__dict__ for i in self.students]}

        with open('Student.json', 'a') as f:
            d = json.dumps(data, indent=2)
            f.write(",\n")
            f.write(d)
            f.write(']')

        # with open('Student.json', 'r+') as f:
        #     data = json.load(f)
        #     data.append(add)
        #     # f.seek(len(f)-1)
        #
        # with open('Student.json', 'w') as f:
        #     d = json.dumps(data, indent=2)
        #     f.write(d)

    def remove_student(self):
        inp = int(input("Enter roll"))
        count = len(self.students)
        self.students = [s for s in self.students if s.roll != inp]
        if count == len(self.students):
            print("Student not found")
            return
        data = {'name': self.name, 'students': [i.__dict__ for i in self.students]}

        with open('Student.json', 'a') as f:
            d = json.dumps(data, indent=2)
            f.write(",\n")
            f.write(d)
            f.write(']')

        print("Student removed")


#     def __add__(self, other):
#         add = Grade(f'{self.name}  {other.name}')
#         add.students = [*self.students, *other.students]
#
#
# c1 = Grade('Grade 1')
# grade_1 = c1.students.append((Student('Himalaya', 'Subedi', 1, 11, 'Science')))
s = Student('Himal', 'Subedi', 1, 11, 'Science')
g = Grade('Grade 1', s.first_name, s.last_name, s.roll, s.age, s.major)
g.list_students()
# g.add_student()
g.remove_student()
