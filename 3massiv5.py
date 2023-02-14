#Задан целочисленный массив. Вывести индексы тех элементов, значения
#которых больше, чем у стоящих справа от него. Определить количество
#таких чисел

a = []
n = int(input('Massiv olshemin kirtin: '))
count = 0
for i in range(n):
    a.append(int(input('Massiv manis berin: ')))
for k in range(n - 1):
    if a[k] > a[k + 1]:
        print("Indeksi: ", k)
        count += 1
print("Sani: ", count)