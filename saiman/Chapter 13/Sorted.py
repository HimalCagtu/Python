# animals = ['Bear', 'Bird', 'Lion', 'Liger', 'Donkcey', 'Bat', 'Dog', 'Camel', 'Elephant']
# print(sorted(animals, reverse=True))
#
# person = {
#     'name': 'Himal',
#     'age': 12,
#     'occupation': 'Software Engineer'
# }
#
# sorte=sorted(person.items())
# print(sorte)
#
# for k,v in sorte:
#     print(k,v)
#
#
# students = [
#     ('John', 2),
#     ('Eve', 4),
#     ('Jennifer', 3),
#     ('Adam', 1)
#     ]
# print(sorted(students,key= lambda x:x[1]))
# employee = {
#     'name': 'John doe',
#     'age': 20,
#     'occupation': 'student',
#     'temporary address': 'Jpani'
# }
# print(sorted(employee))

# for i, j in employee.items():
#     print(i, '-', *[j])
#
set_to_be_sorted = {0, 8, 6, 5, 7, 9, 3, 8, 2, 1, 4, 3, 7, 6, 4, 3, 8, 3, 5, 3}
print(sorted(set_to_be_sorted, reverse=True))

lst = [0, 8, 6, 5, 7, 9, 3, 8, 2, 1, 4, 3, 7, 6, 4, 3, 8, 3, 5, 3]

for i in lst:
    print(lst[i])

lst_of_interns = [(1, 'Saiman Khatiwada'),
                  (2, 'Dipesh Bhattarai'),
                  (3, 'Soyuj Bharadwaj Wagle'),
                  (4, 'Shardul Basnet'),
                  (5, 'Suraj Rajbanshi'),
                  (6, 'Shashank Upadhyay'),
                  (7, 'Himal Subedi')
                  ]


print(sorted(lst_of_interns,key= lambda x:x[0]))
