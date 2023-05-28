class Rectangle:
    length = 25
    width = 33

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def l_o_D(self):
        return (self.width ** 2 + self.length ** 2) ** (1 / 2)


class Circle:
    radius = 45
    PI = 3.14

    def area(self):
        return self.radius * 2 * self.PI

    def circumference(self):
        return self.PI * (self.radius) ** 2

    def diameter(self):
        return 2 * self.radius


class Box:
    height = 15
    width = 20
    length = 33

    def surface_area(self):
        return 2 * (self.height * self.width) + 2 * (self.height * self.length) + 2 * (self.width * self.length)

    def volume(self):
        return self.height * self.width * self.length




b1=Box()
print(b1.volume())

c1=Circle()
print(c1.circumference())

r1=Rectangle()
print(r1.l_o_D())