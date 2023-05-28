class Item:

    def __init__(self, name, rate, quantity):
        self.name = name
        self.rate = rate
        self.quantity = quantity

    def rturn(self):
        return self.name, self.rate, self.quantity


class Bill:
    items = []

    def __init__(self, customer_name, *items: Item):
        self.customer_name = customer_name
        self.items = items

    def count_items(self):
        return len(self.items)

    def total(self):
        p1=i1.rate*i1.quantity
        p2 = i2.rate * i2.quantity
        p3 = i3.rate * i3.quantity
        print('+','-'*60,'+')
        print('|','Himal\' SHOP'.center(60),'|')
        print('+', '-' * 60, '+')
        print('|',f'Order invoice for {b1.customer_name}'.ljust(60),'|')
        print('+', '-' * 60, '+')
        print('|', f'SN  name'.ljust(31),f'       rate  Quantity  total'.ljust(28),'|')
        for i,j in enumerate(b1.items,1):
            print(f"|  {i}  {j.name.ljust(22)}  {str(j.rate).rjust(17)}  {j.quantity}  {str(j.rate*j.quantity).rjust(8)}  |")
        print('+', '-' * 60, '+')
        print('|', f'Grand total ${p1+p2+p3}'.rjust(60), '|')
        print('+', '-' * 60, '+')
        print('|', 'Thank you for visiting Himal SHOP'.center(60), '|')
        print('+', '-' * 60, '+')




i1 = Item('Rice', 2.4, 5)
i2 = Item('Apple', 1, 1)
i3 = Item('notebook',1.5,3)

b1 = Bill('Himal', i1, i2, i3)
print(b1.count_items())
b1.total()


num_of_items=int(input("Enter the number of items you want to buy"))

while num_of_items>0:
    name=input("Enter the name of items")
    rate=float(input("Enter the rate"))
    quantity=float(input('Enter the quantity'))

    item=Bill('Himal',name,rate,quantity)

    num_of_items-=1

print(item)