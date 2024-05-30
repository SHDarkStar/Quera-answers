#https://quera.org/problemset/3405
inputs = list()
while True:
    current = input()
    if current == "0":
        break
    inputs.append(current)
for i in range(len(inputs)):
    rev_inputs = inputs[::-1]
    print(rev_inputs[i])