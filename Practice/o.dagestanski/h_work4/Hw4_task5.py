# Определим словарь животных ключ:значение
d=dict({"dog" : "Шарик", "cat" : "Мурка", "bird" : "Кеша", "tiger" : "шерхан"})
# Создадим шаблон строки
from string import Template
s = Template(" Домашние питомцы $dog и $cat играли во дворе, а попугай $bird сидел в клетке.")
# заменим в строке вхождения шаблонов на их значения из словаря
print(s.substitute(d))

