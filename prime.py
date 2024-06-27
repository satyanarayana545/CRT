# #prime number using while else
# n=int(input("Enter a number"))
# i=2
# while i<=n//2:
#     if n%i==0:
#         print("not a prime")
#         break
#     i+=1
# else:
#     print("prime")
# #prime number using for loop
n=int(input("Enter"))#6
count=0
for i in range(1,n+1):#i=1,i=2,i=3
    if n%i==0:# 6%1==0,6%2==0,6%3==0
        count+=1#c=1,c=2,c=3
if count==2:
    print("prime")
else:
    print("not prime")