#https://quera.org/problemset/221462
list_x = []
list_y = []
list_z = []
count_d_x = {}
count_d_y = {}
count_d_z = {}
for _ in range(7):
    a = input()
    x, y, z = a.split(" ")
    list_x.append(int(x))
    list_y.append(int(y))
    list_z.append(int(z))
for i in list_x:
    if i in count_d_x:
        count_d_x[i] += 1
    else:
        count_d_x[i] = 1
for j in list_y:
    if j in count_d_y:
        count_d_y[j] += 1
    else:
        count_d_y[j] = 1
for k in list_z:
    if k in count_d_z:
        count_d_z[k] += 1
    else:
        count_d_z[k] = 1

min_rep_num_x = min(count_d_x, key=count_d_x.get)
min_rep_num_y = min(count_d_y, key=count_d_y.get)
min_rep_num_z = min(count_d_z, key=count_d_z.get)
print(min_rep_num_x , min_rep_num_y , min_rep_num_z)