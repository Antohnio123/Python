import datetime
import time
class Timer:
    def __enter__(self):
        self.t1=datetime.datetime.now()
    def __exit__(self, exc_type, exc_val, exc_tb):
        t2 = datetime.datetime.now()
        print("Время исполнения кода ")
        print(t2-self.t1)

with Timer():
 time.sleep(3)