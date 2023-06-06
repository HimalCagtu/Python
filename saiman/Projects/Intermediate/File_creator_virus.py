import platform


class Profile:

    def __init__(self, name, syssoft):
        self.name = name
        self.syssoft = syssoft
        # print(f'Hello {self.name} using {self.age}')

    def __str__(self):
        return self.name, self.syssoft


class Virus(Profile):

    def __init__(self, name, syssoft):
        super().__init__(name=name, syssoft=syssoft)

    def create_virus(self):
        print("Infection")
        to_write = f'HEllo {self.name} using {self.syssoft}\n because of your ' \
                   f'stupidity,\nYour system has been infected with a virus'

        with open('Virus.exe', 'w+') as file:
            file.write(to_write)

        with open('Virus.exe', 'r') as f:
            print(f.read())

        # with open(('Virus.exe'))


print('=' * 60)
print('|', "Welcome To File Creator Virus".center(56), '|')
print('+' * 60)
print('|', "Enter the name, User".ljust(56), '|')
name = input()

system = platform.platform()

p1 = Profile(name, system)
print('+' * 60)
print('|', 'Do you want to infect your system? [YES/NO]'.center(56), '|')
user_inp = input().lower()
while True:
    if user_inp == 'yes':
        print('|', 'Wish Granted'.center(56), '|')
        v1 = Virus(p1.name, p1.syssoft)
        v1.create_virus()
    elif user_inp == 'no':
        print('|', 'Good Decision'.center(56), '|')
        exit()
