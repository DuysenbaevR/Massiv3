#Дана целочисленная матрица А[n,m]. Посчитать количество элементов
#матрицы, превосходящих среднее арифметическое значение элементов
#матрицы. Принять n=4, m=5.
import random

a = [[random.randrange(10) for _ in range(5)] for _ in range(4)]
for i in a:
    print(*i)
sum = 0
for k in range(4):
    for j in range(5):
        sum += a[k][j]
print(f"Orta arifmetigi: {sum/20}")
count = 0
for t in range(4):
    for h in range(5):
        if a[t][h] > sum/20:
            count += 1
print(f"Orta arifmetikten ulken {count} dana san bar")