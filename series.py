#1^3+2^2+3^3+.............+20^2==?
res=0
for i in range(1,21):
    if i%2==0:
        res+=i**2
    else:
        res-=i**2
print(res)