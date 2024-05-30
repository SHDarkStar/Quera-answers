#https://quera.org/problemset/3538
n_p1 = int(input())
p1 = input().split()
n_p2 = int(input())
p2 = input().split()
n_p3 = int(input())
p3 = input().split()
l = p1 + p2 + p3
board = ['shanbe', '1shanbe', '2shanbe', '3shanbe', '4shanbe', '5shanbe', 'jome']
result = 7
if 'shanbe' in l:
    result -= 1
if '1shanbe' in l:
    result -= 1
if '2shanbe' in l:
    result -= 1
if '3shanbe' in l:
    result -= 1
if '4shanbe' in l:
    result -= 1
if '5shanbe' in l:
    result -= 1
if 'jome' in l:
    result -= 1
print(result)