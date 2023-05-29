
with open('Personal Details.txt','w') as f:
    f.write("Himal Subedi\nAccount number = 0200014232100011")

# file=open('Personal Details.txt', 'r')
# print(file.read())
# # file.close()
#

#


append="\nBlood Group = B+\nHobby = None"

with open('Personal Details.txt','r+') as f:
    print()
    f.read()
    f.write(append)


file=open('Personal Details.txt','r')
for l in file:
    print(l)