#https://quera.org/problemset/178600
mob_sh = int(input())
fot_sh = int(input())
mob_n = int(input())
fot_n = int(input())
d_sh = mob_sh - fot_sh
d_n = mob_n - fot_n
if d_n > d_sh:
    print('Namakestan')
if d_sh > d_n:
    print('Shekarestan')
if d_n == d_sh:
    print('Equal')