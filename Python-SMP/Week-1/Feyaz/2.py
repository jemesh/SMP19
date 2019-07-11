"""
Making the sorting program first
"""

a=[2,3,1,8,6,5,9,0,7,4]
n=10
for i in range(n):
	for j in range(n-i-1):
		if a[j]>a[j+1]:
			a[j], a[j+1]=a[j+1], a[j]
print(a)

"""
Making the searching program first
"""
search = 3
for i in range(n):
	if a[i]==search:
		print("found at "+ str(i))