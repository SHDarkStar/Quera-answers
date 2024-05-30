#https://quera.org/problemset/232024
def check(h):
    n = len(h)
    middle = n // 2

    for i in range(middle - 1):
        if h[i] >= h[i + 1]:
            return 1
    for i in range(middle, n - 1):
        if h[i] <= h[i + 1]:
            return 2
    return 0


t = int(input())
for i in range(t):
    h = list(map(int, input().split()))
    print(check(h))
