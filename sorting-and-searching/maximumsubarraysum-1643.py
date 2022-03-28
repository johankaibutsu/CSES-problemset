I=input
n = int(I())
ls = [int(i) for i in I().split()]
 
lm = 0
oa = ls[0]
 
for i in range(n):
    lm = max(ls[i],lm + ls[i])
    oa = max(lm,oa)
 
print(oa)