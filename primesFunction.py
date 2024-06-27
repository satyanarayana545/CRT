def isprime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
        return True
for num in[2,3,4,5,6,7,8]:
    if isprime(num) == True:
        print(num)                               