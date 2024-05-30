#https://quera.org/problemset/80651
def valid_team(x, y):
    if x == y:
        return x
    else:
        if x > y:
            return y
        else:
            return x
x = int(input())
y = int(input())
z = int(input())
k = int(input())
a = int(input())
b = int(input())
print(valid_team(x ,y) + valid_team(z ,k) + valid_team(a ,b))