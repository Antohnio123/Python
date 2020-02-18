import time
import random

class Pupil():
    def Solve_Task(self):
        time.sleep(random.uniform(3,6))
        return "Not yet ready"

vivod_Pupil=[Pupil()]
for vivod in vivod_Pupil:
    print(vivod.Solve_Task())
