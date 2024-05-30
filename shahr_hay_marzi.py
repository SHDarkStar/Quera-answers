#https://quera.org/problemset/228669
n = int(input())
m = int(input())
if n == 1:
    print(m)
elif m == 1:
    print(n)
elif n == 1 and m == 1:
    print(1)
else:
    print((m*2)+((n-2)*2))