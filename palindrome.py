n=int(input("Enter a number: "))
s=0
n1=n
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if n1==s:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")