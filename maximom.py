#https://quera.org/problemset/588
n = int(input())
numbers = map(int, input().split())
num_list = list(numbers)
num_list.sort()
print(num_list[n - 1])