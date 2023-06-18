class Shape:

    def __init__(self,side1 , side2):
        self.side1 = side1
        self.side2 = side2



    def get_area(self):

        print(f'{self.side1 * self.side2}')




class Square(Shape):

    def __init__(self,side1,side2):

        super().__init__(side1=side1,side2=side1)


    def get_area(self):

        print(f'{self.side1*self.side1}')




class Rectangle:
    def __init__(self,side1,side2):

        pass
    def get_area(self):
        print(f'{self.side1*self.side2}')


class Triangle:
    def __init__(self,side1,side2):

        pass
    def get_area(self):
        print(f'{1/2*(self.side1*self.side2)}')
    


options = {

    '1':"Square",
    '2':'Rectangle',
    '3':"Triangle"
}
for i,j in options.items():

    print(*i,':',j)

try:
    inp= input("Enter choice")


except:
    print("Error")


if inp=='1':
    side1=int(input("Enter side 1"))
    side2 = int(input("Enter side 2"))
    s1=Square(side1,side2)
    s1.get_area()



# sp=Shape(23,23)
# s1 = Square(sp.side1,sp.side1)
# s1.get_area()

