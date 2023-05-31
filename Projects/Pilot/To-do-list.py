print('=' * 60)
print('|', 'TO-DO LIST'.center(56), '|')
print('|', '+' * 56, '|')
print('|', 'What do you wanna do?'.center(56), '|')
print('|', '1.Write to do list'.center(56), '|')
print('|', '2.ADD to To do List'.center(56), '|')
print('|', '3.READ ONLY'.center(56), '|')
user_choice = int(input())

match user_choice:
    case 1:
        to_do_lst = []
        print('|', 'Enter the number of Task  you have'.center(56), '|')
        no_tasks = int(input())
        for i in range(1, no_tasks + 1):
            i = input(f'Enter the {i}st task')
            to_do_lst.append(i)

        with open('./todolst.txt', 'w') as f:
            f.write(to_do_lst.__str__())

        with open('./todolst.txt', 'r') as f:
            print(f.read())

    case 2:
        with open('to do lst.', 'a+') as f:
            print("Enter the task")
            f.write('Hello')
            read = f.read()

            print(read)

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
