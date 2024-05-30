#https://quera.org/problemset/83360
w = input()
string = list(map(str,input().split()))
c = 0
for i in range(len(string)):
    if w in string[i]:
        c += 1
print(c)