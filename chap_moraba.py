#https://quera.org/problemset/591
n = int(input())
print("*" * n)
for _ in range(n - 2):
    print("*" + (n-2) * " " + "*")
if n > 1:
    print(n * "*")