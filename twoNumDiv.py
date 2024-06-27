n1=int(input("Enter a value: "))
n2=int(input("Enter a value: "))
res=[]
for num in range(20,201):
    if num%n1==0 and num%n2==0:
        res.append(num)
print(res)
