def compare(a,b):
    if a>b:
        print(f"Первое число больше \nОно равно {a}")
    if a==b:
        print(f'Числа равны')
    if b>a:
        print(f"Второе число больше \nОно равно {b}")

a = input(f"Введите первое число")
b = input(f"Введите второе число")
compare(a,b)