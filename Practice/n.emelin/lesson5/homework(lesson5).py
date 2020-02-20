from time import sleep
from random import randint
class Man:
    def __init__(self, name):
        self.name = name
    def solve_task(self):
        return "I`m not ready yet"
human=Man("Nick")
print(human.name, human.solve_task())
class Pupil(Man):
    def solve_task(self):
        sleep(randint(3, 6))
        return "I`m not ready yet"
student = Pupil("Nick")
print(student.name, student.solve_task())