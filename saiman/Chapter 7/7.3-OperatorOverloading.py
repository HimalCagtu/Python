# class ClassRoom:
#      def __init__(self, name):
#         self.name = name
#         self.students = []
#
#      def add_students(self, *students):
#         self.students.extend(students)
#
#      def __add__(self, other):
#         new_classroom = ClassRoom(f'{self.name} and {other.name}')
#         new_classroom.students = [*self.students, *other.students]
#         return new_classroom
#
#
# c1 = ClassRoom('Python')
# c1.add_students('Saiman', 'Suraj', 'Himal')
#
# c2 = ClassRoom('UI/UX')
# c2.add_students('Shardul', 'Shashank')
#
# c3 = c1 + c2
# print(c3.students)
# print(c3.name)

class Adder:

    def __init__(self, *num):
        self.num = num
        self.lst=[]
        self.lst.extend(num)
        print(self.lst)
    def __add__(self, other):

        self.add=self.num+other.num
        print(self.add)


a1=Adder(1,2,3)
a2=Adder(4,5,6)
a1+a2

