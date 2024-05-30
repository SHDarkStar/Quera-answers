#https://quera.org/problemset/91712
x, y = map(int, input().split())
if x == y:
    print('Saal Noo Mobarak!')
else:
    if x > y:
        print(abs(x - y) * 'L')
    if x < y:
        print(abs(x - y) * 'R')