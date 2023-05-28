def make_coffee(sugar=0, beans=0, milk=0):
    # print(sugar,beans,milk)
    water = 250 - milk-sugar-beans
    if milk > 150:
        print("Milk limit exceeded")
    else:
        print(
            f"your coffee is ready with composition of\n\t {water} ml water\n\t {milk} ml milk\n\t "
            f""
            f"Sugar={sugar}\n\t Beans={beans} ")


sugar = int(input("Please enter amount of sugar in spoon\t"))

beans = int(input("Please enter number of beans in spoon\t"))

milk = int(input("Please enter milk in ml\t"))

print(make_coffee(sugar, beans, milk))
