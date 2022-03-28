g=lambda:map(int,input().split())
n,x=g()
d={}
j=0
for v in g():
    j+=1
    if v in d:
        print(d[v],j)
        exit()
    else:
        d[x-v]=j
print('IMPOSSIBLE')