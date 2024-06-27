import copy
arr=[1,2,3,5,7,9,11]

arr1 =copy.deepcopy(arr)
for i in arr:
    if i%2==0:
        arr.remove(i)
print(arr)


