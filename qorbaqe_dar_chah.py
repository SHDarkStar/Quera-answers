#https://quera.org/problemset/235327
import math

t  = int(input())
ans_list = []
for i in range(t):
    a, b, h = map(int, input().split())
    ans = math.ceil(((h - a) / (a - b)) + 1)
    ans_list.append(ans)
for j in range(t):
    print(int(ans_list[j]))