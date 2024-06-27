arr=[1,2,3,4,2,4]
arr2=[]
for i in arr:
    if i not in arr2:
        arr2.append(i)
    else:
        print(i)
