#https://quera.org/problemset/49535
n, v = map(int, input().split())
s = 0
for _ in range(n):
    bottle = int(input())
    s += bottle
if s >= v:
    print('YES')
else:
    print('NO')