from time import sleep
from random import randint


class Man:

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")

class Pupil(Man):

    def solve_task(self):
        sleep(randint(3, 6))
        print("I'm not ready yet")


man_name = input('Enter a name: ')
example_man = Man(man_name)
print(example_man.name)
example_man.solve_task()

pupil_name = input('Enter another name: ')
example_pupil = Pupil(pupil_name)
print(example_pupil.name)
example_pupil.solve_task()
