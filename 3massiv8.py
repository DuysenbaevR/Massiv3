#В матрице А(4-строки,3-столбца) поменять местами наибольшие элементы в первом и третьем столбцах.
import random

a = [[random.randrange(10) for _ in range(3)] for _ in range(4)]
for i in a:
    print(*i)
max = a[0][0]
max2 = a[0][2]
index = 0
index2 = 0
for k in range(3):
    if max < a[k + 1][0]:
        max = a[k + 1][0]
        index = k + 1
    if max2 < a[k + 1][2]:
        max2 = a[k + 1][2]
        index2 = k + 1
a[index][0],a[index2][2]=a[index2][2],a[index][0]
print("/*/*/*/*/*/*/*/*/*")
for i in a:
    print(*i)