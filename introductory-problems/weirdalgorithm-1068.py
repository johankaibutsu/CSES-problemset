def algo(n):
	if n%2==0:
		n =int(n/2)
		return n
	else:
		n = n*3 +1
		return n
 
 
a=int(input())
l=[]
l.append(a)
while (a!=1):
	a=algo(a)
	l.append(a)
for i in range(len(l)):
	print(l[i],end=" ")