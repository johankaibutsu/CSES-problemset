t=int(input())
for i in range (t):
    x,y=input().split(' ')
    if (int(x)+int(y))%3==0 and int(x)/2<=int(y) and int(y)/2<= int(x):
            print('YES')
    else:
        print('NO')