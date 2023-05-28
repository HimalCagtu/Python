def largest_number(a:int,b:int,c:int)->int:

    if a>b>c:
        return a,"is largest"

    elif b>a>c:
        return b,"is largest"


    else:
        return c,"is largest"





a=int(input("Please eneter 1st num"))
b=int(input("Please eneter a num"))
c=int(input("Please enete a num"))

print(largest_number(a,b,c))




