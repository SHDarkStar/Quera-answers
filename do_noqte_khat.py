#https://quera.org/problemset/3414
x, y, i, j = map(int, input().split())
if x == i:
    print('Vertical')
elif y == j:
    print('Horizontal')
else:
    print('Try again')