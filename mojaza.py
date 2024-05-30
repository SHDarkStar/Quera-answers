#https://quera.org/problemset/129726
def separator(ls):
    even =[]
    odd = []
    for n in ls:
        if n % 2 == 0:
            even.append(n)
        elif n % 2 == 1:
            odd.append(n)
    return(even,odd)