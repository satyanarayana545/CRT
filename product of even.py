res=1
for i in range(21,42):
    if i %2 ==0:
        res=res*i
    else:
        res=res/i
print(res)