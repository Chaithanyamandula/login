import re
txt='Akhil is loverboy'
a=re.findall('i',txt)
print('Find all the letter-1',a)
b=re.search("is.*loverboy$",txt)
if b:
    print('Ok')
else:
    print('Not ok')
print('Search the word-is',b)