class Man :
    def __init__(self, name):
        self.name = name

    def solve_task (self):
        return " {}, I`m not ready yet".format(self.name)

name_man = Man (input (" Enter name: "))
print(name_man.solve_task())

from time import sleep
from random import randint
class Pupil(Man) :
    def solve_task (self) :
        print ("Wait.......")
        sleep(randint(3,6))
        return " {}, I`m not ready yet".format(self.name)

name_pupil = Pupil (input (" Enter name: "))
print(name_pupil.solve_task())
