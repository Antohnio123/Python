# Задание 1.
print("Задание 1.")
a1 = list(input("Введите список через запятую: ").split(','))
def lenght(string):
    print(len(string))
lenght(a1)

# Задание 2.
print("Задание 2.")
a2 = list(input("Введите список через запятую: ").split(','))
def reverse(lst):
    b2 = list(reversed(lst))
    print(b2)
reverse(a2)

# Задание 4
print("Задание 4.")
a4 = input("Введите строку с пробелами: ").split(' ')
def to_title(string):
    string = [b4.capitalize() for b4 in string]
    listToStr = ' '.join([str(elem) for elem in string])
    print(listToStr)
to_title(a4)

# Задание 5
print("Задание 5.")
x5 = input("Введите строку, в которой должен быть выполнен подсчет: ")
y5 = input("Введите символ, количество которого надо посчитать в введенной строке: ")
def count_symbol(string, symbol):
    amount = string.count(symbol)
    print(amount)
count_symbol(x5,y5)

# Задание 7.
print("Задание 7.")
from os import path
x7 = input("Введите путь файлу для копирования: ")
y7 = input("Введите куда нужно вставить файл: ")
def copyfile(source, destination):
    if path.exists(source) == 1 and path.exists(destination) == 0 :
        with open(source) as a7:
            with open(destination, "w") as b7:
                for line in a7:
                    b7.write(line)
    elif path.exists(source) == 0 : print("Файла для копирования не существует!")
    elif path.exists(destination) == 1 : print("Невозможно вставить файл: Файл уже существует!")
    else : print("Непредвиденная ошибка")
copyfile(x7,y7)