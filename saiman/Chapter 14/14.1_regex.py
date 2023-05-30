import re

'''regular expressions, also known as regex,
 are a powerful tool for pattern matching and manipulation
  of strings in Python. Python provides a built-in modul
  e called re that allows you to
   work with regular expressions.'''

# sentence = 'The quick brown dog fox jumped over a lazy healthy dog'
# x=re.search('^T.e.*dog$',sentence)
# print(x)

import re

txt = "The rain in 98773197391 9842390198 Spain"

# Check if the string contains any digits (numbers from 0-9):

x = re.findall(r"\d{10}", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
