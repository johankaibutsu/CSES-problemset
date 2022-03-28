I=input
w=c=0
for b,a in sorted((*map(int,I().split()),)[::-1]for _ in" "*int(I())):
 if a>=c:
  c=b
  w+=1
print(w)