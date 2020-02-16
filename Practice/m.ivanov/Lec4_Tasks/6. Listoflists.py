from random import randint


def column_remove(a, x):
    b = list(zip(*a))
    c=[]
    for i in range(len(b)):
        if x not in b[i]:
            c.append(b[i])
    a = list(zip(*c))
    return a


n = int(input('Enter number of rows: '))
m = int(input('Enter number of columns: '))
x = int(input('Enter number: '))#число, столбцы с которым нужно удалить
arr = [[randint(1, 10) for j in range(m)] for i in range(n)]
print(arr)
print(column_remove(arr, x))