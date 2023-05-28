t1=(1,6,9,4,3)

t2=(2,7,8,3,5)


t3=t1+t2
# print(t3)

t4=(*t1,*t2)

print(t4)

# print(type(t1))

enum=tuple(enumerate(t1))
print(enum)