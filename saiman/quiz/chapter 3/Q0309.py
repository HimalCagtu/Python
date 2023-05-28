

car={


'brand':'BMW',
'model':'30A',
'price':300000

}

car['engine']='DTS'



print(car)

add={

    'color':'Red',
    'no_of_sets':2,
    'transmission':'Dual'
}
car.update(add)
print(car)
car.pop('color')
print(car)

car.popitem()
print(car)


for i in car.keys():
    print(i)


for j in car.values():
    print(j)



for k in car.items():
    print(*k)    




