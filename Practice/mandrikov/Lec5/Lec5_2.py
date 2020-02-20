import time
import random


class Pupil:
    def solve_task(self, when):
        self.when = 'I`m not ready yet'


Mike = Pupil()
Mike.solve_task(None)
time.sleep(random.randint(3, 6))
print(Mike.when)