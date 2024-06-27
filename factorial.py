def fact(n):
    res=1
    for i in range(2,n+1):
        res*=i
    return res
re=0
for i in range(1,11):

    re+=fact(i)
print(re)
print(fact(5))