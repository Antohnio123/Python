# Задача 1
print("\nЗадача 1")
s = list(range(0, 101))
x = 0
while x <= len(s):
    if x % 3 == 0:
        s[x] = "Fizz"
    if x % 5 == 0:
        s[x] = "Buzz"
    if x % 15 == 0:
        s[x] = "FizzBuzz"
    x = x + 1
print(s[1:101])

# Задача 2
print("\nЗадача 2")
print("Введите пятизначное число")
s1 = input()
s1 = s1.strip()
s1 = list(s1)
for i in range(0,5):
     print(i + 1, "цифра равна", s1[i])


# Задача 3
print("\nЗадача 3")
s2 = input("Введите числа через пробел: ")
s2 = s2.split(' ')
for i in range(0, len(s2)):
    m = min(s2[i:len(s2)])
    t = s2.index(m)
    a1 = s2.pop(i) #удаление 1 элем
    s2.insert(i, m) #добавл мин элем на 1 место
    s2.pop(t) #удален мин элем
    s2.insert(t, a1) #добавл 1 элем на место мин
print(s2)


# Задача 4
print("\nЗадача 4")
b = "gg\tggg\thhhh\th    hhh"
print(b)
r = b.replace("    ", "%s$") # заменяем 4 пробела на "s"
a = r.expandtabs(tabsize=10) # заменяем символы табуляции на 4 пробела (c tabsize=10 нагляднее)
print(a.replace("%s$", "\t")) # заменяем "s" на символы табуляции









