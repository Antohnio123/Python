number = input("Введите число: ")
lst = list(number)

for i in range(0, len(lst)):
    print(f"{i+1}-ая цифра равна {lst[i]}")
