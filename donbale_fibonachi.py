#https://quera.org/problemset/303
def Fib (num1,num2):
    print(num1)
    num3 = num2 - num1
    num2 = num1
    num1 = num3
    if num1 != 0 and num2 != 0:
        if num1 != 1 or num2 != 1:
            Fib(num1,num2)
num4 = int(input())
Fib(num4,int(input()))
if num4 != 1:
    print(1)