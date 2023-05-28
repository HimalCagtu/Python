class Major:

    def __init__(self, name):
        self.name = name
        self.subjects = []

    def __add__(self, other):
        sub = Major(f'{self.name}+{other.name}')
        sub.subjects = [*self.subjects, *other.subjects]
        return sub


class Subject:

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"subject: {self.name}"

    def __repr__(self) -> str:
        return self.__str__()


mj=Major('science')
mj.subjects.append(Subject('Physics'))
mj.subjects.append(Subject('Chemistry'))


com = Major("Commerce")
com.subjects.append(Subject('Business Mathematics'))
com.subjects.append(Subject('Accounting'))

new_major=mj+com
print(new_major.name)
print(new_major.subjects)