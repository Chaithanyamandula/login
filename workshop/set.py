# s={1,2,False,0,5}
# print(s)
a=int(input())
sum=0
rem=0
while a!=0:
    rem%=10
    sum+=rem*rem*rem
    a=a/10
if a==sum:
    print("Armstrong number")
else:
    print("Not Armstron number")
    