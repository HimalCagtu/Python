word=input("Enter a word [press cancel to exit] : ")

rev=word[::-1]

if rev==word:
    print('palindrome')


else:
    print("not palindrome ")
