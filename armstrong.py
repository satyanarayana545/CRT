n=int(input("Enter a number:"))
c=0
k=n
n1=n
while n>0:
    r=n//10
    c+=1
arm=0
while n1>0:
    r=n1%10
    arm+=r**c
    n1=n1//10
if k==arm:
    print("Armstrong")
else:
    print("not armstrong")