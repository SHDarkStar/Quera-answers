#https://quera.org/problemset/140032
a, b, c, d, e = map(int, input().split())
if a+b>c and a+c>b and b+c>a:
    print('YES')
elif a+d>c and a+c>d and d+c>a:
    print('YES')
elif a+b>d and a+d>b and b+d>a:
    print('YES')
elif a+b>e and a+e>b and b+e>a:
    print('YES')
elif a+e>c and a+c>e and e+c>a:
    print('YES')
elif a+d>e and a+e>d and d+e>a:
    print('YES')
elif b+c>d and b+d>c and c+d>b:
    print('YES')
elif b+c>e and b+e>c and e+c>b:
    print('YES')
elif b+d>e and b+e>d and d+e>b:
    print('YES')
elif c+d>e and c+e>d and d+e>c:
    print('YES')
else:
    print('NO')