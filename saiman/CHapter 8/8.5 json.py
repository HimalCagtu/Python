import json

person = {
    "name": "Himal Subedi",
    'age': 20,
    'married': 'Yes',
    'Occupation': 'Programmer',
    'programming_languages': [
        {
            "name": "Python",
            "version": 3.9,
            'level': "Beginner",
        },
        {
            "name": "Java",
            "version": 17,
            'level': "Expert",
        },
        {
            "name": "C++",
            "version": 2019,
            "level": "Mid",
        },
    ]
}

json_str = json.dumps(person)
print(json_str)
#
with open('Details.json', 'w') as file:
    json.dump(person, file)

json_string = '{"name": "John", "age": 20}'
dict_1 = json.loads(json_string)  # json string in dict format
print((dict_1))

# with open('Details.json','r') as file:
#     dict_1=json.load(file)
#     print(dict_1)

with open('Details.json') as f:
    dict_2 = json.load(f)  # json file as dict
print(dict_2)

# Employee={
#     'name':'Saiman Khatiwada',
#     'ID':2020,
#     'age':30,
#     'address':"Hamsberg",
#     'Expertise':'Hutiyapa',
#     'Experience':'2-years',
#     'Languages':[
#         {
#             'name':'Nepali',
#             'fluency':'A++',
#             'National':True
#
#         },
#         {
#             'name':'English',
#             'fluency': 'A',
#             'National': False
#
#         },
#         {
#             'name': 'Gujrati',
#             'fluency': 'A',
#             'National': False
#
#         }
#
#     ]
#
#
#
# }
#
#
# with open('Details.json','a') as f:
#     json.dump(Employee,f)              # Dict into json file
#
#
#
#
#
#
#
#
