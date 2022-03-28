from bisect import bisect_right
n=int(input())
ls=[int(i) for i in input().split()]
l=[]
ans=0
for i in ls:
	pos=bisect_right(l,i)
	if pos>=ans:
		l+=[i]
		ans+=1
	else:
		l[pos]=i
print(ans)