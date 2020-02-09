"""
Числа - первое задание
"""

seconds = int(input(f"Введите количество секунд прошедших с начала суток: "))
hours = seconds // 3600
minutes = ((seconds / 3600) - hours) * 60
rounded_minutes = int(round(minutes, 0))
print(f"It is {hours} hours {rounded_minutes} minutes.")

"""
Числа - второе задание
"""

d = int(input(f"Введите градус положения часовой стрелки: "))
hours_1 = d // 30
minutes_1 = (d * 12) / 6
if hours_1 !=0:
    if minutes_1 / hours_1 * 60 == 0:
        rounded_minutes_1 = 0
        print(f"It is {hours_1} hours {rounded_minutes_1} minutes.")
    else:
        rounded_minutes_1 = int(round(minutes_1, 0) - (hours_1 * 60))
        print(f"It is {hours_1} hours {rounded_minutes_1} minutes.")
else:
    rounded_minutes_1 = int(round(minutes_1, 0) - (hours_1 * 60))
    print(f"It is {hours_1} hours {rounded_minutes_1} minutes.")

"""
Строки - первое задание
"""

test_string = "Test string for my homework"

print("Строка", test_string)

print("Третий символ строки: ",test_string[2])

print("Предпоследний символ строки: ",test_string[-2])

print("Первые пять символов строки: ",test_string[0:5])

print("Вся строка, кроме последних двух символов: ",test_string[0:-2])

print("С чётными индексами: ",test_string[::2])

print("С нечётными индексами: ",test_string[1::2])

print("В обратном порядке: ",test_string[::-1])

print("Через один в обратном порядке: ",test_string[-1::-2])

print("Длина строки: ",len(test_string))

"""
Строки - второе задание
"""
test_string_4 = "low how how how how how low"
print(test_string_4)
change = "h"
l = len(test_string_4)
count = test_string_4.count(change,0,l)
test_string_4 = test_string_4.replace(change, change.capitalize(), count-1)
test_string_4 = test_string_4.replace(change.capitalize(), change, 1)
print(test_string_4)

"""
Строки - третье задание
"""

test_string_2 = "Test string"
print(test_string_2)
test_string_3 = test_string_2.split()
test_string_2 = str(test_string_3[1] + " " +test_string_3[0])
print(test_string_2)
print(test_string_2.capitalize())








