num=list(range(100))
print(num)
sum=0
square=[]
# for i in num:
#     # print(i)
#
#     sum=sum+i
# print(sum)
#     # print(i)

# for i in num:
#     square.append(i**2)
#
#     y=i**2
#     sum=sum+y
# print(sum)
#
# print(square)
#
# asn=[]
# for x in num:
#     y=x**2+2*x+2
#     asn.append(y)

for i in num:
    sum=sum+i
    avg=sum/len(num)

print(avg)

y=0
for i in num:
    y = (i** 2 + 2 * i + 2)+y
print(y)

print(num)