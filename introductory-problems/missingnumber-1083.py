n = int(input())
 
a = n*(n+1)//2 - sum([int(i) for i in input().split()])
 
print(a)