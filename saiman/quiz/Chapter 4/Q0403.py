celsius=int(input("Please Enter your body temperature"))


fahrenheit=9/5*celsius +32
t=fahrenheit



if t < 96:
    print("low temperature")

elif t>=96 and t<=98:
    print('Normal temperature')

elif t>=99 and t<=101:
    print('Normal fever')

elif t>=102 and t<=104:
    print("high fever")

else:
    print("critical")