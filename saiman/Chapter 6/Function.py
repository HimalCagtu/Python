# Some of the characteristics of function are as follows:
#
#     a block of code that runs when it is called
#     provides organized, reusable and modular code
#     used for reducing duplicates
#     takes zero or more parameters as arguments
#     returns either a value or None
#     returns a tuple when multiple values needs to be returned
#     declared using def keyword
#     it can have any type of arguments eg: int, float, list, Callable or even object
#     unlike other programming languages, python function body can not be empty. If we want to create an empty function body, we can use pass statement.
#     similar to branching and loops, function body also needs indented code block.
def himal_function(a,b,c):


             print(a,b,c)

# PEP 8 Guidelines for defining a python function
#
#     python functions are created using snake_case names
#     top level functions are separated with 2 blank lines
#     parameters inside functions are separated by comma, along with spaces
#     we should not surround = with spaces while using named parameters and default vaues.
#     python function argument type is hinted with the type using :
#     function return type is hinted with right arrow (- and > sign). i.e. ->

# def print_call(a,b):
#     print("call me to print this statement")
#     print("The sum of {} and {} is {}".format(a,b,a+b))
#
# print("I am always executed")
# print_call(4,3)
#
#


# def call_me(a:int,b:int):
#     return a+b
#
#
# y=call_me(2,3)
#
#
# def i():
#     print(y)
#
# i()



# def sum_result(a:int,b:int)->int:
#     return  a+b
#
# c=int(input("enter a"))
# d=int(input("Enter b"))
# print(f"The sum of {c} and {d} is",sum_result(c,d))


# def simple_interest(principal:float,time:int,rate:float)->float: #type hinting in function
#
#     return (principal*time*rate)/100
#
#
#
# p=float(input("Enter the principal sum\n\t"))
# t=int(input("Enter the time\n\t"))
# r=float(input(("Enter the interest rate")))
# Si=simple_interest(p,t,r)
# print(f"The simple interest for {p} for time {t} and rate{r} will be",Si)
# print("total amount to be paid is",Si+p)
#

# def loop_function(a:int)->int:
#     sum=0
#     for i in range(1,a+1):
#         sum=sum+i
#
#     return sum
#
# #
#
# num=int(input("Enter a number  to find its sum from 1 to the number\n\t"))
# print(loop_function(num))
#
#


# def double_triple(num:int)->int:
#     global even
#     global odd
#     if num%2==0:
#         even='even'
#         return num*2
#     else:
#         odd='odd'
#         return num*3
#
#
#
#
# num=int(input("please enter a number"))
#
# if num%2==0:
#     print(f"The result is {double_triple(num)} and number you entered is {even}")
#
# else:
#     print((f'The result is {double_triple(num)} and number you entered is {odd}'))



x=20
print("Initial",x)
def non_local():
    x=10


    def inner_non_local():
        nonlocal x
        x=50
        # print("The inner function doesnot replace the global variable while using non local",x)
        return x

    print("This does not affect the global value of x",inner_non_local())
    return x
print("After replacing",non_local())




