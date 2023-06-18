# class Person:

#     count:int=0
#     name=''

#     def __init__(self,name:str,age:int)->None:

#         self.name:str = name
#         self.age:int = age
#         self.count +=1


#     def greet(self)->str:

#         return f'Hi , {self.name}'


# p1 = Person('Suraj',20)
# p2 = Person('Himal',122)
# # print(p1.greet())
# # print(p1.count)
# print(Person.name)

# # class Person:

# #     def __init__(self, name:str, age:int)->None:

# #         self.name:int = name
# #         self.age:int = age 

# #     def age(self):
# #         return f'{self.age}'


# #     @classmethod

# #     def create_anonymous(cls):

# #         return Person('HI',12)


# # a1 = Person.create_anonymous()
# # print(a1.age)


# # class TempConverter:

# #     @staticmethod
# #     def celsius_to_fahrenheit(c:float)->float:

# #         return f'The temperature is {9*c/5 +32} fahrenheit'

# #     def fahrenheit_to_celsius(f:float)->float:

# #         return f'The temperature is {5*(f-32) / 9} celsius'

# # print(TempConverter.celsius_to_fahrenheit(0))


# class Employee(Person):
#     count = 0

#     def __init__(self,name:Person,age:Person,job_title:str)->None:
#         super().__init__(name,age)
#         self.job_title = job_title

#     def greet_hello(self):

#         return f'I am a {self.job_title}'

    





# e1 = Employee('Suraj', 21 , 'Dev')

# print(e1.greet(), e1.greet_hello())

# # print(isinstance(e1,Employee))
# # print(Employee.__sizeof__)
# print(Employee.count)
# setattr(Employee,'count',10)
# print(Employee.count)

# setattr(Person,'Total',100)
# print(Person.Total)
# # delattr(Employee,'Total')
# # print(Employee.Total)

# print(Employee.__dict__)


# class Coffee:

#     def __init__(self, name:str, price:int)->None:
#         self.name = name
#         self.price = price

#     def check_budget(self, budget:(float, int))->bool:
#         if budget < 0:
#             print("Not enough")
#             exit()
#         if budget !=isinstance(int,float):
#             print("Not acceptable")


#     def get_change(self,budget)->(int,float):

#         return budget - self.price


#     def sell(self, budget):
#         self.check_budget(budget)
#         if budget >= self.price:
#             print(f'Buy {self.name}')

#             if budget == self.price:
#                 print("Success")

#             else:
#                 print(f'Here is change {self.get_change(budget)}')



# c1 = Coffee('Small', 5)
# c2 = Coffee('Regular', 10)
# c3 = Coffee('Big', 15)


# try:
#     inp = float(input("Enter your budget"))


# except:
#     print ("Price should be in num")


# for i in [c3, c2 ,c1]:

#     i.sell(inp)




# import time
# class Vehicle:

#     def __init__(self,name:str,price:int, mileage:int)->None:

#         self.name = name
#         self.price = price
#         self.mileage = mileage


#     def check_budget(self, budget)->str:

#         if not isinstance(budget,int):
#             print("I cannot convert str to int")
#             exit()
        
#         if budget < 0:
#             print('You are broke')
#             exit()
# Vehicle=[bus = Vehicle('bus', 1000000),
# car = Vehicle('car',100000),
# bike = Vehicle('Bike', 10000),
# ]
# Vehicle=[bus = Vehicle('bus', 1000000),
# car = Vehicle('car',100000),
# bike = Vehicle('Bike', 10000),
# ]

#             self.check_budget(budget)

#             if budget >= self.price:
#                 print(f'You can buy {self.name}')

#                 if budget == self.price:
#                     print("Thanks for the purchase")

#                 else:
#                    print( f'you will get {self.return_change(budget)}')
#                 exit("thanks for your transcation")
#             else:
#                 print(f"you cannot buy {self.name} \n checking for another vehicle")
#                 time.sleep(3)
# bus = Vehicle('bus', 1000000,10)
# car = Vehicle('car',100000,12)
# bike = Vehicle('Bike', 10000,22)


# budget = int(input("Enter budget"))

# for vehicle in [bus, car, bike]:
#     vehicle.sell(budget)
































