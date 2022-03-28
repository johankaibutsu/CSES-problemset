P=print
def R(i,a,b):
 if i:
  c=6-a-b
  R(i-1,a,c)
  P(a,c)
  R(i-1,b,a)
n=int(input())
P(2**n-1)
R(n,1,2)