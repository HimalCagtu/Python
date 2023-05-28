person={
'name:str':'Himal',
'age:int':26,
'profession:str':'NH',
'married:bool':True



}
print(person['name:str'])
age=person.copy()

person['age:int']+=10

print(f'old age was {age["age:int"]} and new age is {person["age:int"]}')

# try:
#     print(person['employed'])

# except:
#     print(ValueError)

print(person.get('employed',False))
print(person['employed'])  #shows keyerror 'employed'




