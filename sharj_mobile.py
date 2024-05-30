#https://quera.org/problemset/17244
def charge(n):
    if n == 0:
        return 0
    else:
        return n + charge(n - 1)
n = int(input())
result = charge(n)
print(result)