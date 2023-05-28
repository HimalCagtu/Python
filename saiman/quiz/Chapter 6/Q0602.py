def char_count(name):
    uppercount=0

    lowercount=0
    spacecount=0
    for i in name:
        if i.isupper():
            uppercount+=1

        if i.islower():
            lowercount+=1

        if i.isspace():
            spacecount+=1
    c=(uppercount,lowercount,spacecount)
    print(c)





name=input('Please enter your name')
print(char_count(name))