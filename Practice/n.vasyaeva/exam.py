print("Задание 1")
l = list(input("введите список через пробел:").split(" "))
l.append("%a@b#")
f = l.index("%a@b#")
print("Длина списка = ", f)

print("\nЗадание 2")
sp = list(input("введите список через пробел:").split(" "))
dl = f = len(sp) - 1
h = 0
while 0 < dl:
    t = sp.pop(f)
    sp.insert(h, t)
    dl = dl - 1
    h += 1
print(sp)





