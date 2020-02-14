from random import randint


def sorting(a):#функция сортировки выбором
    for i in range(len(a)):
        m = (a[i:].index(min(a[i:]))) + i
        a[i], a[m] = a[m], a[i]
    return a

def sorting1(a):#вариант не полностью соответствующий условиям задания. элементы не меняются местами, а переносятся в соответствующий интервал
    for i in range(len(a)):
        a.insert(i, a.pop(a.index(min(a[i:]))))
    return a

n = int(input('Enter array length: '))
arr = [randint(1, 100) for j in range(n)]#создание массива случайных чисел длины n
print(arr)
print(sorting(arr))
