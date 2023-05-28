# details=['Himal',33,"back",22,201,'raju','random',101,'High']

# # for i in details:
# #     print(i)

# print(details[:4]) #slicing (Assign it to a variable for ease)

# details[0]="suraj"
# print(details)

# details[1:5]=[223,'End',32,301]
# print(details)
# print(details.__len__())# returns the length
# print(len(details)) #

# details.append("onAcid")# adds new item to the desired index of the lists
# print(len(details))



# details[0]='saiman'

# print(details)
# add=['wagle',22]
# details.extend(add) # adds more than one item
# for a in details:
#     print(a)


# details.pop(-1)

# for a in details:
#     print(a)

# details.insert('shardul',-)# adds new item to the end ot the lists
# print(len(details))


list1=[1,0,3,5,4,6,7,9,8,0] #generally whenever we assign a value of list to another one, it references the older list. Whenever we try to change the content of a list, it eventually changes the value of the older list too. to avoid this, we need to create a shallow copy of the list. To do so, we need to use copy() method.
list2=list1.copy()
list2.append(-1)
print(list1)
list2.reverse() #reverse function
print(list2)

list1.sort() #sort
print(list1)

list1.sort(reverse=True) #sorts as a reverse(descending)
print(list1)

print(list1.count(0))

l1=[2,3,5,7,7,8,9]
l1[3]=6  #for replacing
print(l1)