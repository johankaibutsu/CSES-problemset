I=input
I()
m=o=i=0
O={}
for k in I().split():
 o=max(o,O.get(k,0))
 i+=1
 m=max(m,i-o)
 O[k]=i
print(m)