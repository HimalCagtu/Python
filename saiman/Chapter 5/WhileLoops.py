# while looop - executes until the condition satisfies
#continue - one time skip for certain cases
#break -terminate the loop completely
import sys

# h=0

# while h<20:
#     print(h)
#     h+=1





# name_list=[]
# name=''

# name.lower()

# while name !='exit':

#     name=input("ENter name\n\t")
#     name_list.append(name)

# print(name_list[:-1])

# x=int(input("Enter age"))

# while x<18:
#     # print("THe current value is {}".format(x))
#     x+=1
#     if x==2:
#         continue

#     else:
#         print("The value is{}".format(x))


    
# else:
#     print("welcome")




#
# offensive=['dog','shit','Bullshit','ugly','short']
# highly_offensive=['mast','shit','damn','beat']
#
# while True:
#     word=input("please enter the word")
#     word.lower()
#
#     if word in offensive:
#         print(f'you entered offensive word {word[0]}{"*"* (len(word)-1)} so fo')
#         continue
#     if word in highly_offensive:
#         print("goodbye")
#         break
#     if word==word[::-1]:
#         print('palindrome')
#
#     else:
#         print("not palindrome")





num =3
while num<=6:

    mul=1

    while mul<=10:
        res=mul*num
        print(res)
        mul+=1

    num+=1






import time

hour=0

while True:
    minute=0
    while minute<60:
        seconds=0
        while seconds<60:
            time.sleep(1)
            times=f'Time Elapsed: {hour:0>2} : {minute:0>2} : {seconds:0>2}'
            seconds+=1
            print(times)
            if hour==00:
                if minute==00:
                    if seconds==10:
                        print("Alarm")

        minute+=1

    hour+=1

    int=40
















