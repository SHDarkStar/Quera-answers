#https://quera.org/problemset/232026

t = int(input())
nums = []
recursion = [2, 1, 3, 2, 2, 1, 3, 2]
for _ in range(t):
    n = int(input())
    nums.append(n)
for x in nums:
    y = recursion[(x - 1) % 8]
    if x != 1 and x % 2 != 0:
        y *= -1
    print(y)
