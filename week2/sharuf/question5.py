a = int(input("Enter the number of lines"))
b = a
for i in range(0, a):
    print()
    for x in range(0, b): print(" ", end="")
    for j in range(0, int(2*i+1)):
        print("*", end="")
    b = b-1




