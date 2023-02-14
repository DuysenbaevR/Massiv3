#Задан целочисленный массив. Определить, образуют ли значения его
#элементов арифметическую прогрессию. Если «да» – вывести разность
#прогрессии, если «нет» – ответ «не образуют».

a = []
n = int(input('Massiv olshemin kiritin: '))
for i in range(n):
    a.append(int(input("Manis kiritin: ")))
check = True
d = 0
for k in range(n - 1):
    if a[k] > a[k + 1]:
        check = True
        d = a[k + 1] - a[k]
    elif a[k] < a[k + 1]:
        check = True
        d = a[k + 1] - a[k]
    else:
        check = False
if check == True:
    print('Ayirmasi: ', d)
else:
    print('Arifmetik progressiya emes!')