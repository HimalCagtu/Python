my_list:list=[]
my_list.append(5)
my_list.append(9)

for i in my_list:
    print(i)


# take=int(input("Enter number to add to the list"))
# print(take)
# # take=int(take)

# take=input("input a number")

# my_list.append(int(take))
# print(my_list)



more_items=[4,46,00]

my_list.extend(more_items)
print(my_list)


len=len(my_list)

print("The length is "+str(len))

mylist1=my_list.copy()

my_list.pop(1)

print("before is"+str(my_list)+"after is"+str(mylist1))



