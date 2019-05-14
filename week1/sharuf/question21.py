list=[1,9,3,5,88,46,43,27]
n=len(list)
for i in range(1,n):
    for j in range(0,n-i):
        if(list[j]>list[j+1]):
           temp=list[j]
           list[j]=list[j+1]
           list[j+1]=temp

print("list after sorting is :- \n")
print(list)

