arr=[1,2,3,5,7,9,11]
isDeleted=False
for i in arr:
    if i%2==0:
        arr.remove(i)
        isDeleted=True
        break
if isDeleted==True:
    print("NOT same")
else:
    print("same")



