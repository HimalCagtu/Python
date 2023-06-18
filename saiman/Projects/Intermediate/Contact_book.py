import json
import re

eml = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
phn = r'^\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'


class Contact:

    def __init__(self, name, email, phone):
        self.name: str = name
        self.email: str = email
        self.phone: int = phone


class ContactBook:
    # contact_list: list[all] = []

    def __init__(self):
        pass

    @staticmethod
    def phone_check(phone):
        if (re.fullmatch(phn, phone)):
            print("valid")
        else:
            exit()

    @staticmethod
    def check_mail(email):

        if (re.fullmatch(eml, email)):
            print("proceeding")

        else:
            print(f'{email} is a invalid email ', 'exiting')
            exit()

    def again(self):
        print('|', "Do you want to add/view?".ljust(56), '|')
        print('|', "1.Add".ljust(56), '|')
        print('|', "2.Table  view".ljust(56), '|')
        print('|', "3.List view".ljust(56), '|')
        try:
            choice = int(input())
            if choice == 1:
                self.add()
            elif choice == 2:
                self.view_contacts()

            elif choice==3:
                self.listview()
            else:
                exit()
        except ValueError:
            print(ValueError)
            exit()

    def add(self):
        print('|', "Enter  First name only".ljust(56), '|')
        self.name = input()
        print('|', "Enter Email".ljust(56), '|')
        self.email = input()
        print('|', "Enter Phone".ljust(56), '|')
        self.phone = int(input())
        self.check_mail(self.email)
        add = Contact(self.name, self.email, self.phone)
        # self.contact_list.append(add)
        data = (self.name,
                self.email,
                self.phone)

        with open('list.json', mode='r') as f:
            feeds = json.load(f)
            # feeds = [feeds]

        with open('list.json', 'w') as f:
            feeds.append(data)
            f.write('\n')
            json.dump(feeds, f)
            # f.write(',')
            # f.write(d)
            # f.write(']')
        self.again()

    def view_contacts(self):
        print(('+' * 60))
        print('|', 'SN'.ljust(12), 'Name'.ljust(10), 'Email'.ljust(18), 'Phone'.ljust(13), '|')
        # print(type())
        with open('list.json', 'r') as f:
            d = json.load(f)
            # print(type(d))
            for k, i in enumerate(d, 1):
                print('|', f'{k}'.ljust(12), f'{i[0]}'.ljust(10), f'{i[1]}'.ljust(18), f'{i[2]}'.ljust(13), '|')
        print(('+' * 60))

    def listview(self):
        with open('list.json', 'r') as f:
            d = json.load(f)


            for i in d:
                print('+', '-' * 56, '+')
                print('|', f'🙍{i[0]}'.ljust(56), '|')
                print('|', f' 📧{i[1]}'.ljust(56), '|')
                print('|', f'📞{i[2]}'.ljust(56), '|')
                print('+', '-' * 56, '+')

    def invalidinput(self):
        print("Wrong choice")
        self.view()

    def main_view(self):
        print('=' * 60)
        print('|', 'Contact Book'.center(56), '|')
        print(('+' * 60))
        print('|', 'Choose an option'.center(56), '|')
        print(('+' * 60))
        print('|', '1.Add Contacts'.center(56), '|')
        print('|', ''.center(56), '|')
        print('|', '2.Table View contacts'.center(56), '|')
        print('|', ''.center(56), '|')
        print('|', '3.List View contacts'.center(56), '|')
        print('|', '+' * 56, '|')
        self.view()

    def view(self):
        try:
            choice = int(input())
            if choice == 1:
                self.add()

            elif choice == 2:
                self.view_contacts()
            elif choice == 3:
                self.listview()
            else:
                self.invalidinput()


        except ValueError as e:
            print("Error", e)
            self.view()


c1 = ContactBook()
c1.main_view()

# listview()
