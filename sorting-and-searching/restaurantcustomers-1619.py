N=int
I=input
T=[]
for h in[0]*N(I()):
 a,b=I().split()
 T+=N(a)<<1,N(b)<<1|1
c=h
for t in sorted(T):
 c+=1-t%2*2
 if c>h:h=c
print(h)