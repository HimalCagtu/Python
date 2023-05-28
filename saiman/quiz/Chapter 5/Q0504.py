
num=int(input("Please Enter a number"))
positive=[]
if num<1:
    exit("Enter positive number")

else:
    for i in range(1,num+1):

        if num%i==0:
            positive.append(i)


    print(positive)