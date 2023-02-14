#1 0 1 0 1
#0 1 1 1 0
#1 1 0 1 1
#0 1 1 1 0
#1 0 1 0 1

a = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            continue
        elif (i + j) % 2 == 0 or i == 2 or j == 2:
            a[i][j] = 1
for k in a:
    print(*k)