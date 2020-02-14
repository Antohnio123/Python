from random import randint


def column_remove(a, x):
    for i in range(len(a)):
        while x in a[i]:
            j = a[i].index(x)
            b = list(zip(*a))[:j] + list(zip(*a))[j + 1:]#не нашёл метод для итерации по столбцам, поэтому транспонируем матрицу и собираем её без строки с числом x
            a = list(zip(*b))#возвращаем матрицу к исходному виду
    return a


n = int(input('Enter number of rows: '))
m = int(input('Enter number of columns: '))
x = int(input('Enter number: '))#число, столбцы с которым нужно удалить
arr = [[randint(1, 10) for j in range(m)] for i in range(n)]
print(arr)
print(column_remove(arr, x))