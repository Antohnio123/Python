import math

d=310 #угол
h=math.floor(d/30) #часы
m1=(d-(h*30))//6 #минуты без часов
print("часовая стрелка повернулась " + str(d) + " градусов")
print("Это " + str(h) + " часов и " + str(m1) + " минут")