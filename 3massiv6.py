#8) Отсортировать по возрастанию элементов последней строки целочисленный двухмерный массив 3×4.
import random

a = [[random.randrange(20) for _ in range(3)]for _ in range(4)]
print(a)
a[3].sort()
print(a)