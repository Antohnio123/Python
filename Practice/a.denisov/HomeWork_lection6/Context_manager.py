import time


class MyContextManager:

    def __enter__(self):
        self.t = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Estimated time: {time.time() - self.t}")
