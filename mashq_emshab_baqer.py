#https://quera.org/problemset/10230
a, b, c = map(int, input().split())
if a + b + c == 180 and a!=0 and b!=0 and c!=0:
    print('Yes')
else:
    print('No')