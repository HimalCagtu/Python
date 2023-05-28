num_list=[1,2,3,4,5,6,7,8,9]
new=[]
# odd=[number for number in num_list if number%2==0]

# print(odd)


word='ABCDE'

ASC=[ord(i) for i in word]
print(ASC)


x= range(65,70)

y=[ chr(i) for i in x]

print(y)







cc=range(1,100)

even={ i  for i in cc if i%2==0}
print(even)

dict=range(1,5)
dict={ k: k*4     for k in dict}

print(dict
      )

#fpr generator comprehension use tuple expresion