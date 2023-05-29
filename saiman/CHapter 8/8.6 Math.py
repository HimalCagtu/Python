import math,numpy

# Approximation function in math module
# round function

print(round(0.49))  # rounded down
print(round(1.513))  # rounded up
print(round(1.5113, 3))  # rounded up in the third decimal , 13 is rounded to 1

# floor function (largest int less than or equal to the provided number

print(math.floor(5.56))
print(math.floor(-5.54))  # -6, less than -5
print(math.floor(4.0))  # Prints int, 4

# ceil function (smallest int greater than the provided number )

print(math.ceil(5.56))  # 6
print(math.ceil(-5.56))  # -5
print(math.ceil(5.0))  # 5

# trunc function (removes/drops the fractional part of the floating point number )
# floor if positive number, ceil if negative number

print(math.trunc(5.56))  # prints 5
print(math.trunc(-5.56))  # prints -5

#  math function takes angles in radians but not in degrees.
# formula :
# 1PI*radians=180,  1/2*PI^c = 90


#  trigonometric functions that are available in python math module

#  math.sin(), math.cos(), math.tan()
# math.asin(), math.acos(), math.atan()
print(1 / math.sin(0.5))
print(math.asin(0.5))

# math.dist() (used to find distance between two points)
a = (1, 2)
b = (2, 1)

print(math.dist(a, b))
print(math.sqrt(2))

print(math.degrees(math.radians(360)))

# Powers and exponential

# print(numpy.cbrt(27))
print(math.sqrt(36))
print(math.pow(27, 1/3))
print(math.exp(2))
print(math.expm1(1))

