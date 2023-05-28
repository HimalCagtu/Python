def linear_equation(x: int) -> int:
    if x % 2 == 0 & x % 3 == 0:
        y = x ** 3 + 4 * x ** 2 + 5 * x + 6

        return y
    elif x % 3 == 0:
        y = x ** 3 + 4 * x + 5
        return y
    elif x % 2 == 0:
        y = x ** 2 + 2 * x + 3
        return y

    else:
        return x.__neg__()


x = int(input("Please enter a number\n\t"))
print(linear_equation(x))
