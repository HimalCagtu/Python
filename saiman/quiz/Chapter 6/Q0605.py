def pali_indrome():






    while True:
        print("="*21+f'[Palindrome Finder]'.center(10)+'='*22)
        word = input("Enter a word: ")
        rev = word[::-1]


        if rev==word:

            print('+' + '-' * 60 + '+')
            print(f'|', f'The word {word} is a palindrome'.center(58),f'|')
            print('+' + '-' * 60 + '+')
        else:
            print('+' + '-' * 60 + '+')
            print(f'|', f'The word {word} is not a palindrome'.center(58),f'|')
            print('+' + '-' * 60 + '+')

        inp = input("Do you want to play again?[yes,no]")

        if inp == 'no':
            break



pali_indrome()
print("="*21+f'[Exiting now]'.center(10)+'='*22)


