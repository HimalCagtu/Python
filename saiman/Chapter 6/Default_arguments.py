# While defining function, we can add default values to some or all pa
# rameters so that it takes default value when we do not pass values while calling the function.
# We need to add default parameters only after required parameters are added otherwise it raises an exception



# def add_numbers(b,c,a=0)->int:
#
#     print(a)
#     print(b)
#     print(c)
#     return a+b+c
#
# print(add_numbers(2,3))
#
def greet(key='np'):
    word={
        'np':'namaskar',
        'fr':'Bonjour',
        'en':'Hello'
    }
    print(word[key])

greet()
greet('fr')
greet('en')



