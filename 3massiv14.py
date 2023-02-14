#Дан двухмерный массив, содержащий 8 строк и 8 столбцов. Элементами
#массива являются целые числа. Упорядочить массив по возрастанию
#элементов побочной диагонали.
import random

n = int(input('n: '))
a = [[random.randrange(10) for _ in range(n)] for _ in range(n)]
for k in a:
    print(*k)
print("/*/*/*/*/*/*/*/*/")
for j in range(0, n - 1):
    if a[j][n - j] > a[j + 1][n - j - 1]:
        temp = a[j][n - j]
        a[j][n - j] = a[j + 1][n - j - 1]
        a[j + 1][n - j - 1] = temp
for l in a:
    print(*l)