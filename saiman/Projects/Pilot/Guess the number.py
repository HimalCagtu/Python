import random

print('=' * 60)
print('|', 'GUESS THE NUMBER'.center(56), '|')

count = 0
while True:

    print('+' * 60)
    print('|', 'Enter  Number Between ONE and FIVE'.center(56), '|')
    print('|', ''.center(56), '|')
    print('+' * 60)
    print('|', 'You will have 10 chances to Guess'.center(56), '|')
    print('|', ''.center(56), '|')

    while True:
        com_num = random.randint(1, 10)
        # print(com_num)
        print('+' * 60)
        user_num = int(input('\t'))
        if user_num == com_num:
            print('|', 'You won the game'.center(56), '|')
            print('+' * 60)
            print('|', "Do you want to play again ? [YES/NO] ".center(56), '|')
            print('+' * 60)
            user_choice = input().lower()
            if user_choice == 'no':
                exit()
            else:
                break
        else:
            count += 1
            print('|', f'You have {10 - count} choices'.center(56), '|')
            print('+' * 60)
            print('|', "Enter again".center(56), '|')
            print('+' * 60)

            if count == 10:
                print('+' * 60)
                print("Out of chances".center(56))
                print('+' * 60)
                print("Do you want to play again ? [YES/NO] ".center(56))
                user_choice = input().lower()
                if user_choice == 'no':
                    exit()
                else:
                    count = 0
                    print(count)
                    break
