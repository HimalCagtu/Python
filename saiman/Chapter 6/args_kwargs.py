#*args[variable argument]
#normal arguments should be passed before *args

#kwargs [keyword arguments][also varibale length]
#[stores in key value pair form]
#used with loops

# def add_number(a,b,*args:int)->int:
#
#     sum=a+b
#
#     for i in args:
#         sum=sum+i
#     return sum
#
#
#
#
# print(add_number(2,3,5,6,3,4))

def dic_tionary(name,age,**kwargs): #we must iterate through kwargs as well
    print(name,':',age)
    for keys,values in kwargs.items():

        print(f'{keys} : {values}')





dic_tionary('saiman',23,role='backend')



def tes_t(arg,*args):

    print("First value is {} ".format(arg))

    for a in args:
        print(f"Next value is {a} ")



tes_t(17,177,1777,17777)





























