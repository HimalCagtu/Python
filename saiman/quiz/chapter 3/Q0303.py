multi=[
    [121,52,37],
    [46,51,16],
    [17,82,39]
]



print(multi[-1][-2])


len=len(multi)
print(len)

ap=[40,61,10]

multi.append(ap)
print(str(multi) +"\n")


for i in multi:
    
    for j in i:
        print(j)


multi.clear()
print(multi)