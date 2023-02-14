#11) Дан двухмерный массив 5×6. Определить среднее арифметическое каждого столбца, определить максимум и минимум каждой строки.
import random

a = [[random.randrange(10) for _ in range(6)] for _ in range(5)]
for i in a:
    print(*i)
arif = 0
sum = 0
for k in range(6):
    sum = 0
    for j in range(5):
        sum += a[j][k]
    print(f"{k + 1} - bagana orta arifmetigi: {sum/5}")
for p in range(5):
    print(f"{p + 1} - qatar max: {max(a[p])}, min: {min(a[p])}")