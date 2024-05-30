#https://quera.org/problemset/234249
stones = input().split()
s = list(''.join(stones))
n = str(input())
my_list = list(s)
if n in my_list:
    index = my_list.index(n)
    if index == 0:
        print(6)
    else:
        print(len(my_list[index:]))