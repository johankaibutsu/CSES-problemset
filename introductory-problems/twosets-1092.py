n = int(input())
total = int(n * (n + 1) / 2)
if total & 1:
    print('NO')
else:
    set1, set2 = [], []
    half = total // 2
    while n > 0:
        if half - n >= 0:
            set1.append(n)
            half -= n
        else:
            set2.append(n)
        n -= 1
    print('YES')
    print(len(set1))
    print(' '.join(str(num) for num in set1))
    print(len(set2))
    print(' '.join(str(num) for num in set2))