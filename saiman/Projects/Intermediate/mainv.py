from .Contact_book import *

def main_view():
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
    ContactBook.view()


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
