import datetime

a = datetime.datetime.today().strftime("%Y %m %d")
print(a)  # 'гг мм дд'

today = datetime.datetime.today()
print(today.strftime("%m/%d/%Y"))  # 'мм/дд/гг'

print(today.strftime("Дата %Y-%m-%d Время %H.%M.%S:"))

print(today.strftime("%S"))

h = (today.strftime("%H"))
print("h " + h)
m = (today.strftime("%M"))
print("m " + m)
s = (today.strftime("%S"))
print("s " + s)
t = h + m + s

print(t)
print("----------------")
print("Идем, Дальше")
print("--------------")



# String

home = "Сдесь должен быть умный текст но я не предумал"
print("Ну что Начнем))) ", home)
print("--------------")

print("Третий символ,дай угадаю): ",home[2])

print("--------------")
print("Предпоследний ммм - будет : ",home[-2])

print("--------------")
print("Угадай что скажу по первым 5 буквам: ",home[0:5])

print("--------------")
print("Похоже забыл последние 2 буквы: ",home[0:-2])
print("--------------")

print("На первый второй расчетайсь(каждый 2-й выйти из строя): ",home[::2])

print("--------------")
print("Теперь что были первыми:",home[1::2])

print("--------------")
print("агя абаб(это Баба-Яга), а ты свое прочитаеш с конца) : ",home[::-1])

print("--------------")
print("Умные попались а если с конца да через один: ",home[-1::-2])

print("--------------")
print("А что короче нельзя это-же сколько букв: ",len(home))

print("----------------------------------------------------")
print("Жесть, Идем дальше")

#обмен местами слов
c = "цензор запрещен"
s = c.find(" ")
print(c[s + 1:len(c)], c[0:s])
