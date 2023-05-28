# # # even=tuple(range(0,100,2))
# # #
# # # print(even)
# # #
# # #
# # # name=input("enter name")
# # #
# # # for i in name:
# # #     print(f'{i},',ord(i))
# # #
# # import time
# #
# # odd_list=[]
# #
# #
# # for i in range(0,5):
# #     odd = int(input("Enter a odd number"))
# #     if odd%2==1:
# #         odd_list.append(odd)
# #         i+=1
# #
# #
# # print(odd_list)
# #
# # double=[]
# # for list in odd_list:
# #     double.append(list*2)
# #
# #     print(f'list Double of  {list} is',double)
# #
# #
# #
# # for i in double:
# #     time.sleep(1)
# #     print('\r',i,end='')
# #
# # def locationerror():
# #     print("Error")
#
# dict={
#     'name':'Himal',
#     'age':100,
#     'location':'ratnagiri'
#
#
# }
#
# for key,values in dict.items():
#     print(key,values)



#
#


# lst={'back':['saiman','suraj',"himal0"],
#
# 'front':['n','o','n','e']}
#
# for i in lst:
#     print(f'The {i} developers are\n\t')
#     for j in lst[i]:
#      print(j,'\n')



heroes=['RObert downey','scarlett johansson','chris hensworth']
name=['iron','black widow','God of thunder']


zip=list(zip(heroes,name))
print(zip)







