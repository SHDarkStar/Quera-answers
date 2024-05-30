#https://quera.org/problemset/232025
n = int(input())
winners = []
for i in range(n):
    score_q = 0
    score_c = 0
    t = int(input())
    score = list(input())
    for j in score:
        if j == 'Q':
            score_q += 1
        if j == 'C':
            score_c += 1
    if score_q > score_c:
        winners.append('Quera')
    if score_c > score_q:
        winners.append('CodeCup')
for i in range(len(winners)):
    print(winners[i])