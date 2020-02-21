#1

class Man:

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I am not ready yet.")

man1 = Man("David")

print(man1.name)
man1.solve_task()

print()


#2

import time
import random

class Pupil(Man):

    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print("I am thinking...")

p = Pupil("Bobbi")

print(p.name)
p.solve_task()

