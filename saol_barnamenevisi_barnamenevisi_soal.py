#https://quera.org/problemset/3408
def reverse(s):
    words = s.split()
    reversed_words = " ".join(reversed(words))
    return reversed_words
n = int(input())
s = input()
result = reverse(s)
print(result)