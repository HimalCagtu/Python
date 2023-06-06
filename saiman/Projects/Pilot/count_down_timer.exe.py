import time


print('=' * 60)
print('|', "COUNT DOWN TIMER".center(56), '|')
print('+' * 60)
print('|', "Enter the hour".ljust(56), '|')
hour = int(input())
print('+' * 60)

print('|', "Enter the minute".ljust(56), '|')
print('+' * 60)
min = int(input())
min-=1
# print('|', "Enter the seconds".ljust(56), '|')
# print('+' * 60)
# sec = int(input())

while True:
    while hour>=0:
        # minute = 10
        while min >= 0:
            seconds = 60
            while seconds > 0:
                time.sleep(1)
                times = f'Time Elapsed: {hour:0>2} : {min:0>2} : {seconds:0>2}'
                seconds -= 1
                print('\r', times, end="")
                if hour == 00:
                    if min == 00:
                        if seconds == 00:
                            print('\n|', "Times up".center(56), '|')
                            exit()

            min -= 1

        hour -= 1

        int = 40
