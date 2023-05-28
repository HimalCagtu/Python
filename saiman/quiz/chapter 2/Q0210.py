import math
number=33

if type(number)==int:
    print("The number is a integer ")




res=100/12

if type(res)==float:

    print("IT's a floating point \n")
    print(res)

else:
    print(False)



x=[1,2,3,4,5]
y=[1,2,3,4,5]
z=x


if x==y and x==z:
    print(True)




zoo=['elephant','tiger','zebra','lion',"wolf"]
# if zoo.index('lion'):
#     print("Lion is present")


# try:
#     zoo.index('horse')
#     print("horse ")


# except ValueError:
#     print("Horse is no")


# animal=input("Which animal do you prefer to watch?")


# if animal in zoo:
#     print("WOW COME AND VISIT")
# else:
#     print("SORRY")


# if 'horse' in zoo:
#     print(True)
# else:
#     print(False)

lst=[2, 3, 5, 7, 11, 13, 17,19]

if 9 in lst:
    print("9 is a prime number")


else:print("9 is not prime")