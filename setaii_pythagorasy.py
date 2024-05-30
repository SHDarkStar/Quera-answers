#https://quera.org/problemset/654
#https://7learn.com/blog/play-with-pythagorean-triplet-in-python
def pythagorasy(n):
    for a in range(1, n):
        b = (n * n - 2 * n * a) // (2 * n - 2 * a)
        c = n - a - b
        if (a * a + b * b == c * c and b > 0 and c > 0):
            print (a, b, c)
            return
    print('Impossible')
n = int(input())
pythagorasy(n)