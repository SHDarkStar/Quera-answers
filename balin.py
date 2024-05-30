#https://quera.org/problemset/175884
def calculate_floor(string):
    floor = 0
    for s in string:
        if s == 'U':
            floor += 1
        elif s == 'D':
            floor -= 1
    return floor