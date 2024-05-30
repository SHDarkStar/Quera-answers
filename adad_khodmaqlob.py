#https://quera.org/problemset/617
n = input()
n_revers = n[::-1]
if n == n_revers:
    print('YES')
else:
    print('NO')