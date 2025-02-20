import re
txt='Akhil is loverboy'
b=re.search("is.*loverboy$",txt)
if b:
    print('Ok')
else:
    print('Not ok')
