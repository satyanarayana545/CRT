n=int(input())
print([num for num in range(1,n) if str(num)==str(num)[::-1]])


