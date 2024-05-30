#https://quera.org/problemset/618
n = int(input())
def diamond(n):
    for i in range(0, n + 1):
        print(' ' * (n - i) + '*' * (2 * i + 1))
    for j in range(n - 1, -1, -1):
        print(' ' * (n - j) + '*' * (2 * j + 1))

diamond(n)