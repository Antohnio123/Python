d = input("Enter how many degrees the clock has shifted")  # Ввод градусов
d = int(d)
if d >= 360:
    print("Enter the number of degrees no more than one turn of the arrow (360)")
else:
    m = d * 2  #Преобразование градусов в минуты и часы
    h = int(m / 60)
    m = int(m - (h * 60))
    print('It is ' + str(h) + ' hours ' + str(m) + ' minutes.')
