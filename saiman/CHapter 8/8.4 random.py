# import random
#
# choice=int(input('Enter a number from 1 to 5'))
# rand=random.randint(1,1000)
# print(rand)
#
# if choice==rand:
#     print("PRo juwadi")
#
# else:
#     print("Better luck next time")
#
#
#
import random

# name='Suraj Rajbanshi'
# print(random.choices(name,k=3))


for k in range(1,10):
    print(random.randint(1,10))



options='123456789ABCD@$%^&*(abcde'
print('2'.join(random.choices(options, k=16)))

user=input("ENter your pass")
