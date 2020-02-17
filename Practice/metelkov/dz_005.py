class Man(object):
    def __init__(self, name):
        self.name = name
        tell = "I'm not ready yet"

    def solve_task(self):
        return print("I'm not ready yet'")

#--------------------
print(' ')
print('zadanie 2')
print(' ')
#--------------------
import time
import random

class Pupil(Man):
    def solve_task(self):
        r = random.choice([3, 6])
        time.sleep(r)
        return print("I'm not ready yet")

men = Man("NameMan")
uchenik = Pupil("UchenikName")
men.solve_task()
uchenik.solve_task()