class Animals:
    legs=4

    @classmethod
    def print_legs(cls):
        print("total no of legs: ",cls.legs)


    def print_legs_1(self):
        print("Total no of legs ",self.legs)



print(Animals.legs)
Animals.legs=2
Animals.print_legs()
Animals().print_legs()

human=Animals()
human.legs=2
human.print_legs()

print(human.legs)



class Length:
    cm=64664
    @staticmethod
    def cm_to_m(value):
        return value/100



    @staticmethod
    def m_to_cm(value):
        return value*100

print(Length.cm_to_m(Length.cm))



