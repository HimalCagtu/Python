# class Mother:
#
#     def __init__(self, hair_color, eye_color):
#         self.hair_color = hair_color
#         self.eye_color = eye_color
#
#     def print1(self):
#         return self.hair_color, self.eye_color
#
#
# class Child(Mother):
#
#     def __init__(self,hair, eye, gender):
#         super().__init__(hair, eye)
#         self.gender=gender
#
#
#
#     def print2(self):
#         print("The child has inherited the {} hair color and {} eye color0".format(self.eye_color, self.hair_color,self.gender))
#
#
# m1 = Mother('Brunett', 'Brown')
# c1=Child(m1.hair_color,m1.eye_color,'male')
# print(c1.print2())
#


# class Vehicle:
#     def des(self):
#         print("I am a vehicle")
#
#
# class Car(Vehicle):
#     def des(self):
#         print("I am a car")
#
#     def speed(self,speed):
#         self.speed=speed
#         print(f"I have {self.speed} km/hr speed")
#
#
#
# c1=Car()
# c1.des()
# c1.speed(22)




class Mother:

    def __init__(self,hair_color,eye_color):
        self.hair_color=hair_color
        self.eye_color=eye_color


    # def print(self):
    #     # print(f'HC={self.hair_color}\nEC={self.eye_color}')


class Father:
    def __init__(self,hair_color,eye_color):
        self.hair_color=hair_color
        self.eye_color=eye_color

    # def print1(self):
    #     # print(f"HC={self.hair_color}\nEC={self.eye_color}")



class Child(Mother,Father):

    def __init__(self, hair_color, eye_color):
        super().__init__(hair_color, eye_color)

    def print3(self):
        print(f" \nCHild\n\n\tHC={self.hair_color}\n\n\tEC={self.eye_color}")




mhc=input("Enter hair color of mother")
mec=input('Enter Eye color of Mother')

m1=Mother(mhc,mec)
# m1.print()
fhc=input("Enter hair color of father")
fec=input("Enter eye color of father")
f1=Father(fhc,fec)
# f1.print1()

c1=Child(f1.hair_color,m1.eye_color)
c1.print3()


























