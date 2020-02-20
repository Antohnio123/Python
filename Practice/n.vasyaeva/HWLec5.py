from time import sleep
from random import randint
print("Задание 1")
class Man:

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        return "I`m not ready yet"

man1 = Man(input("Введите имя:"))
print(man1.name, man1.solve_task())
print("\nЗадание 2")

class Pupil(Man):

    def solve_task(self):
        sleep(randint(3, 6))
        return "I`m not ready yet"

pupil = Pupil(input("Введите имя:"))
print(pupil.name, pupil.solve_task())