# Числа
# 1
print("Enter the number of seconds:")
x = int(input())
hours = x // 3600
minutes = x % 3600 // 60
print("It is", hours, "hours,", minutes, "minutes.")

# 2
print("Enter the number of degrees:")
y = int(input())
n = y // 30 #кол-во часов
m = y % 30 // float('0.5') #кол-во мин
print("It is", n, "hours,", m, "minutes.")

# Строки
# 1
s = "Home work"
print("Третий символ строки -", s[2])
s1 = len(s) # длина строки
print("Предпоследний символ строки -", s[s1 - 2])
print("Первые пять символов строки -", s[0:5])
print("Строка без последних двух символов -", s[0:s1 - 3])
print("Символы с четными индексами - ", s[0:s1:2])
print("Символы с нечетными индексами -", s[1:s1:2])
k = s1 - 1 #индекс последнего символа
s2 = ""
while k >= 0:
    s2 = s2 +s[k]  #строка в обратном порядке
    k = k - 1
print("Все символы в обратном порядке - ", s2)
print("Все символы строки через один в обратном порядке, начиная с последнего -", s2[0:s1:2])
print("Длина данной строки -", s1, "символов.")

# 2
s3 = "Mather hello hello hello"
z = s3.count("h") - 2 #кол-во "h" - 2
t = 0
s4 = ""
while "h" not in s3[t]:
    t = t + 1
else:
    s4 = s3[t + 1:len(s3)]
    print(s3[0:t + 1], s4.replace("h", "H", z))

# 3
k = "hello friend"
n = k.find(" ")
print(k[n + 1:len(k)], k[0:n])