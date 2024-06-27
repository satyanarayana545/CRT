def gcd(num1,num2):
    factors1=[]
    factors2=[]
    cl=[]
    for i in range(2,num1+1):
        if num1%i==0:
            factors1.append(i)
    for i in range(2,num2+2):
        if num2%i==0:
           factors2.append(i)
    print(factors1, factors2)
    for i in factors1:
        for j in factors2: # if i in factors2
            if i == j:
                cl.append(i)
    return cl[-1]
num1=21   
num2=49
res=gcd(21,49)
print(res)
print(f" GCD of {num1} and {num2} is {num1//res}/{num2//res}")
