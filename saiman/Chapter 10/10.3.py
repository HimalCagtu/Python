class MyCustomException(Exception):  # inheriting base class
    pass

class AgeError(Exception):
    min_age = 0
    max_age = 100
    def __init__(self,age, *args):
        super().__init__(*args)
        self.age = age
        if self.age<{self.min_age} & self.age>{self.max_age}:
            print("invalid age")
    def __str__(self):
        return f'{self.age} is not between {self.min_age} and {self.max_age}'




class LengthError(Exception):
    def __init__(self,value,*args):
        super().__init__(*args)
        self.value=value

    def __str__(self):
        return f'The value {self.value} is not possible'


class Length:
    def __init__(self,value):
        if value<0:
            raise LengthError(value)

l1=Length(-2)