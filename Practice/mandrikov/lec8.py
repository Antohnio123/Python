# Задача 2
import random

a = []
for i in range(100):
    a.append(round(random.random() * 50))

i = 1  # обычный вывод для сравнения
while i <= 100:
    print('%4d' % a[i - 1], end='')
    if i % 10 == 0: print()
    i += 1

print()
i = 0  # вывод reversed
while i < 10:
    if i % 2 == 0:
        j = i * 10
        k = j + 9
        while j <= k:
            print('%4d' % a[j], end='')
            j += 1
        print()
    else:
        j = i * 10
        k = j + 9
        while j <= k:
            print('%4d' % a[k], end='')
            k -= 1
        print()
    i += 1

###########################
# Задача 3
def Range(start, stop, step):
    current = start
    step1 = step
    while current <= stop:
        yield current
        current = current + step1

g = Range(1, 16, 3)
for i in g:
    print(i)

######################################33
# Задача 5

string = input('Введите строку')
elem = input('Введите элемент, который хотите найти')
s1 = string.count(elem)
print(s1)