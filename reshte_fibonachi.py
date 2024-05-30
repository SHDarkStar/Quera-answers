#https://quera.org/problemset/17675
def fibo(n):
    fibo_list = [0, 1]
    for _ in range(2, n + 1):
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    return fibo_list

n = int(input())
output_l = []
fibo_list = fibo(n)
for i in range(1, n + 1):
    if i in fibo_list:
        output_l.append('+')
    else:
        output_l.append('-')
output_string = "".join(output_l)
print(output_string)