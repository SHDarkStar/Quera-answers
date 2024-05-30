#https://quera.org/problemset/3429
t = int(input())
if t > 100:
    print("Steam")
elif t < 0:
    print('Ice')
elif 0 <= t <= 100:
    print('Water')