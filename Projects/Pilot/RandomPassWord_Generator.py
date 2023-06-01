import random
import time

options = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+~{}":|::<>|L:{'

print('=' * 60)


def random_password():

    while True:
        print('|', 'Enter the number of characters you want in your password'.center(56), '|')
        print('+' * 60)
        char = int(input())
       
        while True:

            if char < 8:
                print('+' * 60)
                print('|', "At-least 8 characters required".center(56), '|')
                print('+' * 60)
                char = int(input())
            elif 8 <= char <= 16:
                pa_ss = random.choices(options, k=char)
                print( ''.join(pa_ss).ljust(10), "is your computer generated password".center(44))
                print('+' * 60)
                print('|', "Are You Satisfied with this Password? [YES/NO]".center(56), '|')
                print('+' * 60)
                satis = input().lower()
                if satis == 'yes':
                    print('+' * 60)
                    print('|', "Do you want to save this password in a file? [YES/NO]".ljust(56), '|')
                    print('+' * 60)
                    choice = input().lower()
                    if choice == 'yes':
                        with open('pass.txt', 'w') as file:
                            file.write(str(''.join(pa_ss)))
                            print('+' * 60)
                            print('|', "Thanks".center(56), '|')
                            print('+' * 60)
                            break
                    else:
                        print('+' * 60)
                        exit()
                else:
                    print("Do you want same number of characters? [YES/NO]")
                    same_num = input()
                    if same_num == 'yes':
                        print('+' * 60)
                        print('|', "wait".center(56), '|')
                        time.sleep(2)
                        print('+' * 60)
                        print('|', "I am trying my best".center(56), '|')
                        time.sleep(4)
                        print('+' * 60)
                        print('|', 'Almost there'.center(56), '|')
                        time.sleep(4)
                    else:
                        break
            else:
                count = +1
                print(count)
                if count == 10:
                    time.sleep(300)
                    print("|", '5 minutes ban'.center(56), '|')

                else:
                    print('+' * 60)
                    print('|', 'Limit exceeded'.center(56), '|')
                    print('+' * 60)
                    print('|', "At-most 16 characters required".center(56), '|')
                    print('+' * 60)
                    char = int(input())


random_password()
