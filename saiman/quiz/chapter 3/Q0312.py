PI=3.1415

# if you want to convert the floating point data to int use typecasting as



print(str(int(PI)))

str_1="20"
str_2="30"
print(str_1+str_2)


print(str(int(str_1)+int(str_2))) #simple answer is to typecast 



x=['1','2','3','4','5']

sum=0

for i in x:
    i=int(i)
    sum+=i
    
print(sum)





odd=[1,3,5,7,9,11,13,15]
prime=[2,3,5,7,11,13,17]

odd=set(odd)
prime=set(prime)

print(odd.difference(prime))



print((odd.difference(prime)).union(prime.difference(odd)))

print(prime.difference(odd))




