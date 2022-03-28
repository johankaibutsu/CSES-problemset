def s(ls,n):
	r = 1
	for i in range(0,n):
		if ls[i] <= r:
			r=r+ls[i]
		else:
			break
	print(r)
 
x=int(input())
lx=[int(i) for i in input().split()]
lx.sort()
s(lx,x)