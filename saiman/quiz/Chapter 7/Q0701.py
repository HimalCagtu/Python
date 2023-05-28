class Person:
    weight: float = 0

    def __init__(self, name, age, male=True):
        self.name = name
        self.age = age
        self.male = male

    def year_of_birth(self):
        if self.age >= 18:
            print(f'you were born on year {2023 - self.age}\nYou are allowed to drink\n')

        else:
            print("CHild Detected")

    def get_pronouns(self):
        m = ['he', 'his', 'him']
        s = ['she', 'her', 'hers']

        if self.male:
            print("Your pronouns are",m)
        else:
            print("Your pronouns are",s)


name=input("Enter your name\t")
age=int(input("Enter your age\t"))
male=bool(input("Enter True if you are a male\t"))




p1 = Person(name,age,male)
p1.year_of_birth()

p1.get_pronouns()
