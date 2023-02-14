#Дан двухмерный массив 7×7. Найти сумму модулей отрицательных нечетных элементов.

import random
a = [[random.randrange(-10, 10) for _ in range(7)] for _ in range(7)]
for i in a:
    print(*i)
sum = 0
for k in range(7):
    for j in range(7):
        if a[k][j] < 0 and a[k][j] % 2 == 1:
            sum += a[k][j]
print(f"Juwap: {abs(sum)}")