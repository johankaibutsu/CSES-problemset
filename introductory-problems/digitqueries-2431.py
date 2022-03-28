I=input
for i in range(int(I())):
    k=int(I())
    p=1
    d=1
    while k>9*d*p:
        k-=9*d*p
        p*=10
        d+=1
    k-=1
    print(str(p+k//d)[k%d])