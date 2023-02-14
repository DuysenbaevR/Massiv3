#0 0 0 1
#0 0 1 2
#0 1 2 2
#1 2 2 2

n = int(input('n: '))
a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (i + j) == n - 1 :
            a[i][j] = 1
        elif (i + j) > n - 1:
            a[i][j] = 2
for k in a:
    print(*k)