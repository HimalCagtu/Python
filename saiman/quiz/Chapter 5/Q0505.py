import math
num=int(input("Enter a number"))
x=num
fact=math.factorial(num)
# print(fact)
sum=0


while x>0:
    nu=x%10


    sum=sum+math.factorial(nu)
    x=x//10

print(sum)

if num==sum:
    print("special")
else:
    print("not special")





