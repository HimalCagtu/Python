# animals = ['Bear', 'Bird', 'Lion', 'Liger', 'Donkcey', 'Bat', 'Dog', 'Camel', 'Elephant']
# print(sorted(animals, reverse=True))
#
person = {
    'name': 'Himal',
    'age': 12,
    'occupation': 'Software Engineer'
}

sorte=sorted(person.items())
print(sorte)

for k,v in sorte:
    print(k,v)


students = [
    ('John', 2),
    ('Eve', 4),
    ('Jennifer', 3),
    ('Adam', 1)
    ]
print(sorted(students,key= lambda x:x[1]))