from time import time
from time import sleep
class ContextManager :
    def __init__(self,s_t=1):
        self.s_t = s_t
    def __enter__(self):
        t = time()
        sleep(self.s_t)
        return time() - t
    def __exit__(self,exc_type, exc_val, exc_tb) :
        print("Output processed.")
        return 0

with ContextManager(2) as execute_time:
    print("Code execution time : {} sec.". format(execute_time))