age=int(input("Enter positive age number:"))
if age>=1 and age<=5:
    print("You are a kid")
elif age>=6 and age<=10:
    print("You are a child")
elif age>=11 and age<=17:
    print("you r a boy")
elif age>=18 and age<=59:
    print("you r a man")
elif age>=60 and age<=100:
    print("you r a old man")
elif age>100:
    print("Immortal")
else:
    print("Invalid age number")