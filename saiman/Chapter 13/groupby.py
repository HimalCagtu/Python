import itertools
animals = ['Bear','Bird','Lion','Liger', 'Donkcey', 'Bat', 'Dog', 'Camel', 'Elephant','Eesd']
animals = (sorted(animals))
print(animals)
values = itertools.groupby(animals, lambda x:x[1])
# values = itertools.groupby(animals, lambda x:x[0])
grouped={ k:list(v)  for k,v in values}
print(grouped)

