#https://quera.org/problemset/209103

def main():
    num1, num2 = map(int, input().split())
    if num1 == num2:
        for _ in range(num1):
            print(" _ " * num2)
            print("| " * (num1 + 1))
        print(" _ " * num2)
    else:
        for _ in range(num1):
            print(" _ " * (num1 + 1))
            print("| " * (num2 + 1))
        print(" _ " * num2)
if __name__ == "__main__":
    main()
