# lst=[]
#
# for i in range(10):
#     lst.append(i)
#
# print(lst)
#
#
# lst_1=[ 2*num+1 for num in range(10)]
# print((lst_1))
#
#
# dict={num:num**num for num in range(10)}
# print(dict)
#
#
# pattern = [print() or [print(j,end='  ') for j in range(1, i+1)] for i in range(1, 6)]
# x=''
#
# generator=(4*num ** 2 + 3*num - 6 for num in range(1000000))
# #
# # print(generator)
# lis=[4*num ** 2 + 3*num - 6 for num in range(-100,1000)]
# print(lis)
# # print(lis)
#
# if generator.__sizeof__()<lis.__sizeof__():
#     print("size of generator is less",generator.__sizeof__(),lis.__sizeof__())
#
#
#
#


# name='Apple'
# dict={}
# for i,j in enumerate(name):
#     # print(i)
#     k=ord(j)
#     dicts={
#         j:k
#
#     }
#     dict.update(dicts)
# print(dict)
#
# xyz={i:ord(i) for i in ('Apple')}
# print(xyz)

abbreviations = (
    ('ABC', 'Atanasoff Berry Computer'),
    ('BCD', 'Binary Coded Decimal'),
    ('CD', 'Compact Disc'),
    ('DVD', 'Digital Video Disc'),
    ('HTTP', 'Hyper Text Transfer Protocol'),
    ('WWW', 'World Wide Web'),
)

dict={ key:value for key,value in abbreviations}
print(dict)
