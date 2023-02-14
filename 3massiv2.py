#2) Дан массив, состоящий из 12 двоичных чисел.
# Удалить элементы, которые встречаются более двух раз

import random
a = []
n = int(input('Massiv olshemin kiritin: '))
count = 1
for i in range(n):
    a.append(random.randrange(10, 15))
print(a)
print("/*/*/*/*/*/*/*/*/*/*")
for k in range(n - count):
     temp = a[k]
     sum = 0
     for j in range(n - count - 1):
         if temp == a[j + 1]:
             sum += 1
         if sum > 1:
             del a[j]
             count += sum
print(a)