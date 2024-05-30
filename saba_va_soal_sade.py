#https://quera.org/problemset/31025

n, k = map(int, input().split())
for _ in range(k):
    n /= 2
if n < 0 and n != int(n):
    n -= 1
print(int(n))