# length feet to meter
#
class Length:

    def __init__(self, length):
        print(f'The length is {length} meter')
        self.length = length

    @classmethod
    def from_feet(cls, length):
        return cls(length*0.3048)


l1 = Length.from_feet(1)
print(l1.length)
