# Данный пример был запулен т.к. "Идеально рассмотреть разные решения..."(с)
# IMHO: Данное решение, несмотря на кажушуюся простоту и лаконичность, "под капотом" будет выглядеть
#       куда более громоздко, чем "классическое", изложенное в 3.py. А также, это решение мне кажется менее
#       "читабельным".

l = input("Введите последовательность через пробел: ").strip().split()
l = list(map(int, l))

for i in range(len(l)):
    minimum = min(l[i::])
    l[i + (l[i::]).index(minimum)] = l[i]
    l[i] = minimum

print(l)
