## Задача 1
a = list(range(100))
for b in range(100):
    if a[b]%15 == 0:
        a[b] = "FizzBuzz"
    elif a[b]%3 == 0:
        a[b] = "Fizz"
    elif a[b]%5 == 0:
         a[b] = "Buzz"
print(a)

## Задача 2
num = str(input("Введите число"))
if num.isdigit():
    for c in range(len(num)):
        print(str(c+1) + " цифра равна " + num[c])
else: print("Нужно ввести число без посторонних символов")

## Задача 3
arr = input('Введите члены массива для сортировки через запятую:').split(',')
for d in range(len(arr)):
    min = d
    for e in range(d + 1, len(arr)):
        if int(arr[e]) < int(arr[min]):
            min = e
    arr[d], arr[min] = arr[min], arr[d]
print(arr)

## Задача 4
from os import path
dir = input("Введите путь к файлу или строку:\n")
if path.exists(dir):
    f = open(dir, "r+", encoding="utf-8")
    print("Файл найден.")
    g = f.readlines()
    print (g)
    f.close()
    for h in range(0, len(g)):
        g[h] = g[h].replace("    ", "temp")
        g[h] = g[h].replace("\t", "    ")
        g[h] = g[h].replace("temp", "\t")
    f = open(dir, "w", encoding="utf-8")
    print(g)
    f.writelines(g)
    f.close()
else:
    f=dir
    print("Строка опознана.")
    f = f.replace("    ", "temp")
    f = f.replace("\t", "    ")
    f = f.replace("temp", "\t")
    print(f)