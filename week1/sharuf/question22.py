list=[1,9,3,5,88,46,43,27]
n=len(list)
n1=8
n2=46
count=0
for i in range(1,n):
    if(n1==list[i]):
       print(n1,"is found",i,"position")
       count+=1
    if(n2 == list[i]):
       print(n2,'is found in',i,"position")
       count+=1
if(count==0):
  print("entered numbers are not found")
