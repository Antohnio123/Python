from random import randint


n = int(input('Enter number of rows: '))
m = int(input('Enter number of columns: '))
x = int(input('Enter number: '))#число, столбцы с которым нужно удалить
arr = [[randint(1, 10) for j in range(m)] for i in range(n)]
print(arr)
for i in range(n):
    while x in arr[i]:
        a = arr[i].index(x)
        b = list(zip(*arr))[:a] + list(zip(*arr))[a + 1:]#не нашёл метод для итерации по столбцам, поэтому транспонируем матрицу и собираем её без строки с числом m
        arr = list(zip(*b))#возвращаем матрицу к исходному виду
print(arr)