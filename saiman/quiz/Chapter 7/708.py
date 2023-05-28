class Vehicle:
    name = 'Auto'
    brand = 'tvs'
    wheels_count = 4
    engine_type = 'dts-i'
    braking_system = 'Abs'


class HeavyVehicle(Vehicle):
    def __init__(self, wheels_Count, max_load, mileage):
        super().__init__()
        self.wheels_count = wheels_Count
        self.max_load = max_load
        self.mileage = mileage
        print(self.wheels_count, self.mileage, self.max_load, self.engine_type, self.brand, self.braking_system)


class Bike(Vehicle):
    def __init__(self, wheels_count):

        super().__init__()
        self.client = ''

        self.wheels_count = wheels_count

    def get_number_name(self):
        return self.name,self.number

    def set_number_name(self, number, name):
        self.number = number
        self.name = name

    @property
    def passenger(self):
        return self.passenger

    @passenger.setter
    def passenger(self, passenger):
        self.client = passenger


v1 = Vehicle()
# hv=HeavyVehicle(6,150,25)

bk = Bike(2)
bk.set_number_name(120, 'abs')
print(bk.get_number_name())

print(issubclass(Bike, Vehicle))
print(isinstance(v1, Vehicle))
# bk.passenger = 'himal'
