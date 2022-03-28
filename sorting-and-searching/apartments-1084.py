S=sorted
I=lambda:map(int,input().split())
n,m,k=I()
A=S(I())+[1e9]
i=g=0
for b in S(I()):
 while A[i]+k<b:
  i+=1
 if A[i]-k<=b:
  i+=1
  g+=1
print(g)