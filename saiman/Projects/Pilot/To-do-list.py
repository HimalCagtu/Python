import  os
from datetime import *

print('=' * 60)
print('|', 'TO-DO LIST'.center(56), '|')
print('|', '+' * 56, '|')
nme = '| Enter name: '
name = input(nme).capitalize()
print('|', '+' * 56, '|')
print('|', 'What do you wanna do?'.center(56), '|')
print('|', '+' * 56, '|')
print('|', '1.Create new to do list'.ljust(56), '|')
print('|', ''.center(56), '|')
print('|', '2.ADD to existing To do List'.ljust(56), '|')
print('|', ''.center(56), '|')
print('|', '3.READ ONLY'.ljust(56), '|')
print('|', '+' * 56, '|')
user_choice = int(input('  '))
print(os.path.isfile(f'{name}.txt'))
to_do_lst = []
match user_choice:
    case 1:

        print('|', 'Enter the number of Task  you have'.center(56), '|')
        print('|', '+' * 56, '|')
        no_tasks = int(input('\t'))
        for i in range(1, no_tasks + 1):
            print('|', f'Enter the task no {i}'.center(56), '|')
            i = input()
            to_do_lst.append(i)

        with open(f'{name}.txt', 'w+') as f:

            f.write(f'{to_do_lst.__str__()}  Created at : {datetime.today().__str__()}')
            # f.write(str(datetime.today()))

        print('|', "Do you want to view the tasks? [YES/NO] ".center(56), '|')
        choice = input()
        if choice == 'yes':
            with open(f'{name}.txt', 'r') as g:
                print(g.read())
                print('=' * 60)
        else:
            print('|', "Don't Forget to check to-do list".center(56), '|')
            print('=' * 60)
            exit()

    case 2:
        if os.path.isfile(f'./{name}.txt') == False:
            print(f"No to-do list for {name}")
            exit()

        else:
            task_to_add = []
        print('|', 'Enter the number of Task  to add'.center(56), '|')
        no_tasks = int(input())
        for i in range(1, no_tasks + 1):
            i = input(f' Enter the task')
            task_to_add.append(i)
        with open(f'{name}.txt', 'a') as f:
            f.write('\n')
            f.write(f'{str(task_to_add)} , Updated at {str(datetime.today())}')

        print('|', "Do you want to view the tasks? [YES/NO] ".center(56), '|')
        choice = input()
        if choice == 'yes':
            with open(f'{name}.txt', 'r') as f:
                print(f.read())
                print('=' * 60)
        else:
            print('|', "Don't Forget to check to-do list".center(56), '|')
            print('=' * 60)
            exit()

    case 3:
        try:
            with open(f'{name}.txt', 'r') as f:
                print('=' * 60)
                for i in f.readlines():

                    print( f'{i}'.center(56))
                print( "Thanks".center(56))
                print('=' * 60)
        except:
            print('|', f"No Person named {name}".ljust(56), '|')
            print('=' * 60)

    # case 4:
    #     with open(f'{name}.txt','w') as f

# to_do_lst = []
# print('|', 'Enter the number of Task  you have'.center(56), '|')
# no_tasks = int(input())
#
# for i in range(1, no_tasks + 1):
#     i = input(f'Enter the {i}st task')
#     to_do_lst.append(i)
#
# with open('to do lst', 'r') as f:
#     read = f.read()
# print(read)
#