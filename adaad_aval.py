#https://quera.org/problemset/293
def between(s, e, prime):
    print()
    for i in range(s, e + 1):
        if i in prime:
            print(i)

s = int(input())
e = int(input())
prime = []
for i in range(2, e + 1):
    for j in range(2 , i):
        if i % j == 0:
            break
    else:
        prime.append(i)

between(s, e, prime)
