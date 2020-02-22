import time
from timeit import default_timer as timer

class how_time():
    def __enter__(self):
        self.start = timer()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = timer()
        return print(self.end - self.start)


with how_time():
    print(2+2)
    time.sleep(2)
