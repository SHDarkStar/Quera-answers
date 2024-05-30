#https://quera.org/problemset/616
n = int(input())
num_list = []
def pow2(n):
    x = 2
    while x <= n:
        x = x * 2
    return x

print(pow2(n))