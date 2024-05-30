#https://quera.org/problemset/3539
n = list(input())
s = 0
while not len(n) == 1:
    for i in n:
        s += int(i)
    n = list(str(s))
    s = 0
print("".join(n))