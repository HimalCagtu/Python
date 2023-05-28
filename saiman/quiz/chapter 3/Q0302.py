wild=['tiger','lion','deer','bear','zebra']
wild.sort()
print(wild)
wild.reverse()
print(wild)
more=['leopard','elephant','rhino']
wild.extend(more)
print(wild)

i=wild.index('leopard')

wild.pop(i)
print(wild)

wild.insert(2,'leopard')
print(wild)


wild.remove('rhino')
print(wild)