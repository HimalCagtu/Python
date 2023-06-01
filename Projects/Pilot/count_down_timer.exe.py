import time

hour = 0
min = int(input("Enter minutes"))
sec = int(input("Enter seconds"))

while True:
    minute = 10
    while minute > 0:
        seconds = 60
        while seconds > 0:
            time.sleep(1)
            times = f'Time Elapsed: {hour:0>2} : {minute:0>2} : {seconds:0>2}'
            seconds -= 1
            print('\r',times, end="")
            if hour == 00:
                if minute == min:
                    if seconds == sec:
                        print("Times up")
                        exit()

        minute -= 1

    hour -= 1

    int = 40
