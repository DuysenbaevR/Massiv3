#5) Задан целочисленный массив. Определить разность между суммой
#значений элементов массива на участках, где элементы монотонно
#возрастают (каждое следующее число больше предыдущего) и суммой
#значений элементов массива на участках, где элементы монотонно
#убывают (каждое следующее число меньше предыдущего).

import random

n = int(input('Massiv olshemin kiritin: '))
a = []
i = 0
d = 0

for i in range(n):
    a.append(random.randrange(50))
print(a)
print("/*/*/*/*/*/*/*/*/*/*/*/*/*/")
for k in range(n - 1):
    i = 0
    d = 0
    if a[k] < a[k + 1]:
        i = a[k + 1] - a[k]
        print(i)
    else:
        d = a[k] - a[k + 1]
        print(d)