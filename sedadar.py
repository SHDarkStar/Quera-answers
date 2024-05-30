#https://quera.org/problemset/140033
def count_vowels(w):
    vowels = "aeiou"
    c = 0
    for i in w:
        if i in vowels:
            c += 1
    return c

w = input()
result = count_vowels(w)
print(result)