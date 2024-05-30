#https://quera.org/problemset/177664
n = int(input())
d = {}
for _ in range(n):
    people_list = input()
    name, money = people_list.split()
    d[name] = int(money)
sorted_money = sorted(d.items(), key=lambda x: x[1], reverse=True)
if sorted_money:
            max_name, max_money = sorted_money[0]
            print(max_name)