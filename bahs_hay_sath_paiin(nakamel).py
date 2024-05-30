#https://quera.org/problemset/234251
import sys
def set_recursion_limit():
    sys.setrecursionlimit(10**9)
set_recursion_limit()

n, peygir = map(int,input().split())
c_list = []
clients = ['Peygir', 'Tannaz', 'Jeddy', 'Morshed', 'Peygir', 'Tannaz']
n_clients = clients * (n//5)
for i in range(n):
    num = int(input())
    c_list.append(n_clients[num - 1])
for j in range(n):
    print(c_list[j])