import re
txt='abcd are alphabets'
a=re.sub('\s','*',txt)
print(a)