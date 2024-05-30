#https://quera.org/problemset/6082
def count_asterisks(n, m):
    count = 0
    for _ in range(n):
        a = input().split()
        count += a.count('*')
    return count

n, m = map(int, input().split())
ans = count_asterisks(n, m)
print(ans)
