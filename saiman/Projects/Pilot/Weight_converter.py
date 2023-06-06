while True:
    count = 0

    while True:
        print('+' * 56)
        print('|', 'Weight Converter'.center(52), '|')
        print('|','-' * 52,'|')
        print('|', 'Options'.center(52), '|')
        print('|', '-' * 52, '|')
        print('|', '1.Kg to lbs'.center(52), '|')
        print('|', '2.lbs to kg'.center(52), '|')
        print('|', '3.Kg to gram'.center(52), '|')
        print('|', '4.Kg to quin'.center(52), '|')
        print('|', '5.Kg to ton'.center(52), '|')
        print('+' * 56)
        print('|', 'Choose the Option'.center(52), '|')
        print('+' * 56)

        choice = int(input('\t'))
        if choice < 6:
            count = 0
            match choice:
                case 1:
                    print('+' * 56)
                    kg = float(input('Enter weight\t'))
                    print('+' * 56)
                    print('|', f"The {kg} kg is {kg * 2.205} lbs".center(52), '|')
                    print('+' * 56)

                case 2:
                    print('+' * 56)
                    lbs = float(input('Enter weight\t'))
                    print('+' * 56)
                    print('|', f"The {lbs} lbs is {lbs / 2.205} kg".center(52), '|')
                    print('+' * 56)

                case 3:
                    print('+' * 56)
                    kg = float(input('Enter weight\t'))
                    print('+' * 56)
                    print('|', f"The {kg} kg is {kg * 1000} gram".center(52), '|')
                    print('+' * 56)

                case 4:
                    print('+' * 56)
                    kg = float(input('Enter weight\t'))
                    print('+' * 56)
                    print('|', f"The {kg} kg is {kg / 100} quin".center(52), '|')
                    print('+' * 56)

                case 5:
                    print('+' * 56)
                    kg = float(input('Enter weight\t'))
                    print('+' * 56)
                    print('|', f"The {kg} kg is {kg / 907.2} ton".center(52), '|')
                    print('+' * 56)


            print('|', 'Do you want to Convert another unit ?'.center(52), '|')
            print('-' * 56)
            print('|', '\t\tYES'.ljust(48), '|')
            print('|', '\t\t''NO'.ljust(48), '|')
            print('+' * 56)
            choice_1 = input("").lower()

            if choice_1 == 'no':
                print('+' * 56)
                print('|','Thank you for Choosing this Software'.center(52), '|')
                print('+' * 56)
                exit()
        else:

            count += 1
            print('+' * 56)
            print('|', f"Unknown Choice".center(52), '|')
            print('|', ''.center(52), '|')
            if count<4:
                print('|', 'Please Enter another Choice'.center(52), '|')
            print('|', ''.center(52), '|')
            print('+' * 56)

        if count > 3:
            print('|',"Python program cannot handle your B.S \U0001FAE1".center(52),'|')
            exit()

