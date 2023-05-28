class Employee:
    __project = "Homaale"
    __department = 'Backend'
    __salary = 2000000
    __id = 1010
    first_name = 'Cagtu'
    last_name = 'Nepal'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        print(self.__id, self.first_name, self.last_name)


e1 = Employee('Himal', 'Subedi')
# print(e1)
