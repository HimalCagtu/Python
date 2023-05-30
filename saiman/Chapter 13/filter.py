# filter(function, iterable)
'''def is_even(num):
    return num%2==0

list_1 = [1,2,3,4,5,6,7,8,9,10]

list_2 = filter(is_even, list_1)

print(list(list_2))'''


def is_non_negative(num):
    return num > 0


lst = [-9, -7, -6, -4, 1, 3, 13]
app=[]
fltrd = list(filter(is_non_negative, lst))
for i in fltrd:
    app.append(i)

print(app)
print(fltrd)
