import itertools

# animals = ['Bear','Bird','Lion','Liger', 'Donkcey', 'Bat', 'Dog', 'Camel', 'Elephant','Eesd']
# animals = (sorted(animals))
# print(animals)
# values = itertools.groupby(animals, lambda x:x[1])
# # values = itertools.groupby(animals, lambda x:x[0])
# grouped={ k:list(v)  for k,v in values}
# print(grouped)

cars = sorted(('Car1', 'Tesla', 'BMW', 'Audi', 'Urus'))
print(cars)
values = itertools.groupby(cars, lambda x:x[0] )
print(values)

a={ i:tuple(j) for i,j in values }
print(a)

#
# for i,j  in values:
#     print(i,tuple(j))
