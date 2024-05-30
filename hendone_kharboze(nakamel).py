#https://quera.org/problemset/235095
h = int(input())
k = int(input())
h_time = h * 2
k_time = k * 1

if (k % 2 == 0 and h % 2 == 0):
    print('YES')
elif (k % 2 == 0 and h % 2 == 1):
    print("YES")
elif (k == h):
    if (h % 2 == 0):
        print("YES")
    else:
        print("NO")
elif h_time == k_time:
    print("YES")
else:
    print("NO")