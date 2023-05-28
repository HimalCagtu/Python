# def sum_natural(n):
#     sum=0
#     if n>=0:
#         sum=n+sum_natural(n-1)
#
#     return sum
#
#
#
#
# inp:int=int(input("Enter the number"))
#
# print(sum_natural(inp))


#
# def fact(num):
#
#     if num>0:
#         return num*fact(num-1)
#     else:
#         return 1
# inp:int=int(input("Enter the number"))
#
# print(fact(inp))

#
# def sum(num):
#     a = num % 10
#     num //= 10
#     if (num > 0):
#         return a + sum(num)
#     else:
#         return a
#
# # print(sum())
fibo=[]

def fibo_nacci(n:int)->list[int]:


    if n<=2:

        return 1


    else:
        n=(fibo_nacci(n - 1) + fibo_nacci(n - 2))
        
        return n







print(fibo_nacci(7))















