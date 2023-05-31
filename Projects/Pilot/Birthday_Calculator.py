import datetime, math
from datetime import date
def birthday():
    print('=' * 60)
    print('|', 'BIRTH-DAY CALCULATOR'.center(56), '|')
    print('*' * 60)
    print('|', "Enter the Year, Month and Day respectively".center(56), '|')
    print('*' * 60)
    year: int = int(input('\tYear : '))
    month: int = int(input('\tMonth : '))
    day: int = int(input('\tDay : '))

    while True:
        print('*' * 60)
        print('|', "Your Entered date is:".center(56), '|')
        print('|', f'Year : {year} '.rjust(50), '|'.rjust(7))
        print('|', f'Month : {month}'.rjust(48), '|'.rjust(9))
        print('|', f'Day : {day}'.rjust(48), '|'.rjust(9))
        print('*' * 60)
        print('|', "Is this Information correct ? [Yes/No] ".ljust(56), '|')
        print('*' * 60)
        check = input().lower()

        if check == 'yes':
            birth_date = datetime.date(year, month, day)

            fomatted: str = birth_date.strftime('%A')
            print('|', f'You were born on {fomatted}'.center(56), '|')
            current_age = (date.today() - birth_date) / 365
            print('|', f'{current_age.days} years is your age'.center(56), '|')

            # n_b = 365+birth_date.month*30.147 + birth_date.day-date.today().month*30
            # print(n_b,'days')

            if month <= date.today().month:
                next_birthday = birth_date.month * 30.42 + birth_date.day + date.today().month * 30.147 + date.today().day
                print('*' * 60)
                print('|', f'{math.ceil(next_birthday)} days till your birthday'.center(56), '|')
                print('=' * 60)
                exit()
            else:
                next_birthday = month * 30.32 - date.today().month * 30.117 - date.today().day + day
                print('*' * 60)
                print('|', f'{math.ceil(next_birthday)} days approximate till your birthday'.center(56), '|')
                print('=' * 60)
                exit()
        elif check == 'no':
            print('|', "What is incorrect ? [Y/M/D]".ljust(56), '|')
            incorrect = input().lower()

            if incorrect == 'y':
                print('|', "Enter the Year".center(56), '|')
                year: int = int(input())
            elif incorrect == 'm':
                print('|', "Enter the month".center(56), '|')
                month: int = int(input())
            else:
                print('|', "Enter the day".center(56), '|')
                day: int = int(input())


        else :
            print("Option incorrect")
            exit()

birthday()