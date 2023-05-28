
yoda={

    'age':910,
    'species':'Yodas',
    'gender':'male',
    'affilations':['Jedi','Galactic Republic'],
    'master':{

                'name':'Qui-Gon Jinn',
                'age':48,
                 'affilations':['Jedi','Galactic Republic','Heliost Clan'],
                'master':{
                            'name':'Dooku',
                            'age':83,
                            'affilations':['House serenno','Jedi']
                }

    }
}


print(yoda['master']['master']['affilations'][0])
yoda['master']['master']['affilations']='Sith'
print(yoda)

yoda.pop('master')
print(yoda)