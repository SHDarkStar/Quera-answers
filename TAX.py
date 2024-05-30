#https://quera.org/problemset/6313
m = []

while True:
    n = int(input())
    if n == 0:
        break
    else:
        m.append(n)

for i in m:
    if i <= 1000000:
        print(i)
    elif i > 1000000 and i <= 5000000:
        b = int(i / 100) * 10
        print(i-b)
    else:
        b = (i / 100) * 20
        if b != int(b):
            print(i-b)
        else:
            print(int(i-b))