############################ Задача 1
def len_custom(lst):
    i = 0
    for j in lst:
        i += 1
    print(i)

lst_n = [2,4,6,8,10]
len_custom(lst_n)

print()
############################ Задача 2
def rev_custom(lst):
    i = 0
    new_l = []
    for j in lst:
        i += 1
    n = i - 1
    for j in lst:
        new_l.append(lst[n])
        n -= 1
    print(new_l)

rev_custom(lst_n)

print()
############################ Задача 3
def rng(bgn, stp, st):
    lst = []
    k = bgn
    if st > 0 and bgn < stp:
        while k <= stp:
            lst.append(k)
            k += st
    elif st > 0 and bgn > stp:
        print("Так нельзя!")
    elif st < 0 and bgn < stp:
        print("Так нельзя!")
    elif st < 0 and bgn > stp:
        while k >= stp:
            lst.append(k)
            k += st
    elif st == 0:
        print("Шаг не может быть равен нулю!")
    print(lst)

bgn = -13
stp = -10
st = -1

rng(bgn, stp, st)


print()
############################ Задача 4

def to_title(name):
    spl = name.split()
    new_srt = ""
    for i in spl:
        new_srt = new_srt + i.capitalize() + " "
    print(new_srt.rstrip())

srt = 'orlov      Ilya          evgenyevich'
to_title(srt)

print()
############################ Задача 5

def count_symbol(srt, i):
    print(srt.count(i))

srt_l = "Hi, Elvis, I am here!"
count_symbol(srt_l, "e")

print()
############################ Задача 6

# не смог понять как составить алгоритм


print()
############################ Задача 7

import os


def copyfile(src, dstn):
    try:
        with open(src, "r", encoding='utf-8') as f:
            text = f.readlines()
    except FileNotFoundError:
        print("Файл не найден!")
        exit()
    if os.path.exists(dstn):
        ans = input("Файл уже существует. Переписать?(y/n): ")
        if ans == "y":
            with open(dstn, "w", encoding='utf-8') as f:
                f.writelines(text)
                print("Файл скопрован!")

        elif ans == "n":
            exit()
        else:
            print("Введи y или n!")
            ans = input("Файл уже существует. Переписать?(y/n): ")
            if ans == "y":
                try:
                    with open(dstn, "w", encoding='utf-8') as f:
                        f.writelines(text)
                        print("Файл скопрован!")
                except FileNotFoundError:
                    print("Файл не найден!")
            elif ans == "n":
                exit()
    else:
        with open(dstn, "w", encoding='utf-8') as f:
            f.writelines(text)
            print("Файл скопрован!")


source = "in.txt"
destination = "out.txt"

copyfile(source, destination)


print()
############################ Задача 8



print()
############################ Задача 9

class User:
    def __init__(self):
        self.name = ""
        self.age = ""

    def setName(self):
        self.name = input("Введи имя: ")

    def setAge(self):
        self.age = input("Введи возраст: ")

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)

class Worker(User):
    def __init__(self):
        super(Worker, self).__init__()
        self.salary = "0"
    def setSalary(self):
        self.salary = input("Введи зарплату: ")

    def getSalary(self):
        print(self.salary)

w1 = Worker()
w2 = Worker()

w1.name = "John"
w1.age = 25
w1.salary = 1000

w2.name = "Jack"
w2.age = 26
w2.salary = 2000

print("Сумма зарплат = " + str(w1.salary+w2.salary))

