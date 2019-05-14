a=int(input("enter the number of number you want to add"))
b=[]
for i in range(0,a):
    b.append(int(input("enter the number")))
print(b)
print("numbers according to the given condition")
for i in range(0,a):
    if((b[i]**3)%3==1):
       print(b[i])

