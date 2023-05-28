# for i in range(0,5):
#
#     for j in range(0,i+1):
#         print('*',end='')
#     print()
#


# for i in range(1,10):
#     # print(i)
#     if i%2==1:
#        for j in range(1,i+1):
#            if(j%2==1):
#             print(j,end='  ')
#
#        print()



# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end='  ')
#
#
#     print()


#
# for i in range(1,6):
#     for j in reversed(range(1,i+1)):
#         print(j,end='  ')
#
#     print()
#
#
#
# for i in range(1,6):
#     for j in range(1,6):
#         print(j*i,end=' ')
#
#     print()
#
#
#
# word='Apple'.upper()
#
# for i in range(0,5):
#     for j in range(0,i+1):
#         print(word[j],end='  ')
#
#     print()
#



# for i in range(1,6):
#     for j in reversed(range(1,i+1)):
#         print("*",end='  ')
#
#     print()






for i in range(1,10):
        if i%2==1:
            for j in range(1,i+1):
                print('   ' * (5 - j), end='')
                for k in range(j,0,-1):

                     if j%2==1:
                        print(j,end='  ')

            print()