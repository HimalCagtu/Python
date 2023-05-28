# ets are similar to lists except they can contain unique items. Some features of sets are as follows.

#     Sets are similar to lists except they have unique data
#     Sets are represented by comma separated values enclosed within braces {}
#     Sets are not ordered, so we can not access sets using indices.
#     Set items can not be changed individually, but can be added to it or removed from it.
numbers1={20,30,20,20,20,40}

print(numbers1)
numbers1.add(50)
print(numbers1)

numbers1.update({60,70,80})
print(numbers1)



print(numbers1.remove(60))
print(numbers1.discard(60))#Here removing an item with either of the method gives the same result, however if an item does not exist in the set then the reemove() method throws a KeyError.



for i in numbers1:
    print(i)







odd={1,3,5,9,}
even={1,2,4,9}

print(odd.difference(even))


print(even.difference(odd))

print(odd.union(even))

print(odd.intersection(even
                       ))

