class Item:


     def __init__(self, name, rate, quantity):
        self.name = name
        self.rate = rate
        self.quantity = quantity


class Bill:

    def __init__(self, customer_name, *items):
        self.customer_name = customer_name
        self.items = items
        self.itms = []

    def count_items(self):
        for i in self.items:
            self.itms.append(i)

        print(len(self.itms))

    # def total(self):
    #     self.total=i1.rate*i1.quantity
    #     print(f"Total price will be {float(self.total)}")


# num=int(input("Enter the Number of items"))
#
# while num!=0:
#     name=input("Enter the name of the item")
#     rate=float(input("Enter the rate"))
#     quantity=float(input("Enter the quantity"))
#
#     i1=Item(name,rate,quantity)
#     num-=1
#
#
















