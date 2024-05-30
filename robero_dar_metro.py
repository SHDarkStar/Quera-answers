#https://quera.org/problemset/218361
q, w, e, r, t, y, u, i = map(int, input().split())
a, s, d, f, g, h, j, k = map(int, input().split())
sum = 0
for _ in range(1):
    if q == a == 1:
        sum += 1
    if w == s == 1:
        sum += 1
    if e == d == 1:
        sum += 1
    if r == f == 1:
        sum += 1
    if t == g == 1:
        sum += 1
    if y == h == 1:
        sum += 1
    if u == j == 1:
        sum += 1
    if i == k == 1:
        sum += 1
print(sum)