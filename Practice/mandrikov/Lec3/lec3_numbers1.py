k = input("Write number of seconds")  #Ввод секунд
k = int(k)
if k >= 86399:  #Колличество секунд, которое нельзя превысить по условию задачи
    print('Write number of seconds to one day!')
else:
    m = k / 60  # Преобразование секунд в минуты и часы
    h = int(m / 60)
    m = int(m - (h * 60))
    print('It is ' + str(h) + ' hours ' + str(m) + ' minutes.')
