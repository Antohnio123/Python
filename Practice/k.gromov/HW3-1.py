# Задача №1

print("Ведите количество секунд:")  # количество секунд в 1-х сутках
s = int(input())
h = int(round(s / 3600))
m = int(round((s % 3600) / 60))

print("Это", h, end='')

if 5 < h <= 20:
    print(' часов')
else:
    if h % 10 == 1:
        print(' час')
    else:
        if 2 <= h % 10 <= 4:
            print(' часа')
        else:
            print(' час')

print(m, end='')

if 2 <= m <= 20:
    print(' минут')
else:
    if m % 10 == 1:
        print(' минута')
    else:
        if 2 <= m % 10 <= 4:
            print(' минуты')
        else:
            print(' минут')










