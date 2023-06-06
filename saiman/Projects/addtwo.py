# x = '123456.78'
# y = '1234567.89'
# lis_y = []
# lis_x = []
# x = x.split('.')
# print(x)
# # new_list=[]
# for i in x:
#     lis_x.append(int(i))
#     # print(lis_x)
#
# y = y.split('.')
# for i in y:
#     lis_y.append(int(i))
#     # print(lis_y)

# z = f'{lis_x[0] + lis_y[0]}'
# print(str(z), 'is the sum')
# for i in lis_x:
#     if lis_x[0]:
#         for j in lis_y:
#             z = i+j
#         print(z)
# new_list.extend(lis)
# print(lis)
# new_x = ''.join(lis)
# print(new_x.split('.'))
# for i in lis:
#     str += i
# print()
# for i in lis:
#     z = float(i) + 20
#     print(z)

x = '123456.78'
print(len(x))
y = '1234567.89'

lis_x = list(x)
lis_y = list(y)
int_x = (''.join([str(i) for i in lis_x]))

int_x = int_x.split('.')
# print(int_x)
indx=x.index('.')
str_x = ''

for i in int_x:
    str_x += i

print(str_x)

int_y = (''.join([str(i) for i in lis_y]))

int_y = int_y.split('.')
# print(int_y)
str_y = ''

for i in int_y:
    str_y += i

print(str_y)

# for i in str_x:
#     for j in str_y:

