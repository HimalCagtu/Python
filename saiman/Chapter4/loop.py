# for i in(range(1,100)):
    # if i==50:
    #     break

    # else:
    #     print(i)


    # if i%2==0:
    #     print(f'{i} is even')
    
    # else:
    #     print("{} is odd".format(i))

    # if i%2==0 and  i%3==0:
    #     print("BOth by 2 and 3")


    # elif i%2==3:
    #     print("only by 2")
    # elif i%3==0:
    #     print("only by 3")


    # else:
    #     print("Hola")




# name=input("Please enter a name as a string")
# age=22

# match name:
#     case 'Himal':
#         print("Thanks")

#     case '2':
#         print('Error please enter a string ')

#     case _:
#         print("Hmm")


(a,b)=(5,3)

match (a,b):
    case (1,0):
        print()

    case ( _,2):
        print("mathe")

    case(_,3):
        print('xyz') 





x=input("enter height")

height='small' if x < 6 else('medium' if x>6 and x<8) else'large'



