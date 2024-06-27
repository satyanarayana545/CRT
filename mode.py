#mode of 2,2,4,2,8,5,2
arr = [2,2,4,2,8,5,2]
counter = {}
for num in arr:
    if num not in counter:
        counter[num] = arr.count(num)
    max = max(counter.values()) 

for key, val in counter.items():
    if val == max:
        print(f"Mode of {arr} is {key}")
        break