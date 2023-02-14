#0 1 2
#1 2 3
#2 3 4

n = int(input('n: '))
a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = i + j
for k in a:
    print(*k)