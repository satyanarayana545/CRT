n=int(input("Enter a number:"))
s=0
i=1
while i<n:
    if n%i==0:
        s=s+i
    i+=1
if s==n:
    print("Perfect number")
else:
    print("Not a perfect number")