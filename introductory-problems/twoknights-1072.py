n=int(input())
for i in range(1,n+1):
	ans = (i*i*(i*i-1)) - 8*(i-1)*(i-2)
	print(ans//2)