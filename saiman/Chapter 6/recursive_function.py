# def fact(n):
#
#     if n>0:
#        return n*fact(n-1)
#
#     else:return 1
#
#
# num=int(input("Enter a number"))
# print("Factorial is ",fact(num))
#




# def fibo(n):
#
#     if n>1:
#         return fibo(n-1)+fibo(n-2)
#     return  n
#
#
#
# num=int(input("Enter a number"))
# print("Factorial is ",fibo(num))

def con_vert(a):

    if a!=0:
        return bin(a)


print(con_vert(14))