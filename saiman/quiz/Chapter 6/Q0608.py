def sum(*args):
    mul = 0
    div = 0
    for i in args:
        if i % 2 == 1:
            mul = mul + i * 2

        if i % 2 == 0:
            div = div + (i / 2)

    total = mul + div
    print(total)


sum(5,6,7,8)
