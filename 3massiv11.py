#Дана целочисленная матрица размера M × N, элементы которой могут
#принимать значения от 0 до 100. Различные строки матрицы назовем
#похожими, если совпадают множества чисел, встречающихся в этих
#строках. Найти количество строк, похожих на первую строку данной
#матрицы.
import random
m = int(input('M: '))
n = int(input('N: '))

a = [[random.randrange(5) for _ in range(n)] for _ in range(m)]
for i in a:
    print(*i)
count = 0
for k in range(m - 1):
    sum = 0
    for j in range(n):
        if a[0][j] == a[k + 1][j]:
            sum += 1
    if sum == n:
        count += 1
print(f"Birinshi qatarga {count} dana qatar uqsaydi")