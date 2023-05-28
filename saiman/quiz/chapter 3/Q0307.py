Rich={'USA',"China",'Japan','Germany','France','Australia','Italy'}
Europe={'Germany','France','England','Switzerland','Italy','Portugal','Portugal','Sedwen'}

# print(Rich.difference(Europe))
# print(Europe.difference(Rich))
# print(Rich.intersection(Europe))

# print(Rich.union(Europe).difference(Rich.intersection(Europe)))

# print((Rich-Europe).union(Europe-Rich))

# print(Rich.isdisjoint(Europe))
Rich.difference_update(Europe)

print(Rich)


asian_rich={'Japan','China'}

american_rich={'USA','Canada'}

if asian_rich.issubset(Rich):
    print("Asian rich is a subset")


if Rich.issuperset(asian_rich):
    print(True)


print(american_rich.issubset(Rich))
