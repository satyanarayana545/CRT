data = [
    #    name   age  salary id
    ("mahendra", 23, 50000, 100),
    ("gautham", 21, 40000, 101),
    ("hemanth", 29, 39000, 102),
    ("upendra", 30, 50001, 103)
]

#1
data.sort()
for bio in data:
    print(bio)

print()

#2
data.sort(key=lambda x:x[1],reverse=True)
for bio in data:
    print(bio)

print()

#3
"""approach1"""
data.sort(key=lambda x:x[1])
print(data[-1][0])

"""approach2"""
print(max(data, key=lambda x:x[1])[0])

print()
#3
"""approach1"""
data.sort(key=lambda x:x[1])
print(data[0][0])

"""approach2"""
print(min(data, key=lambda x:x[1])[0])

print()
#4
"""approach1"""
data.sort(key=lambda x:x[2])
print(data[-1][0])

"""approach2"""
print(max(data, key=lambda x:x[])[0])
