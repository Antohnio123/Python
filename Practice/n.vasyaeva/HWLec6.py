
print('\nЗадание 1')
def chargen():
    while True:
        for c in "0123456789":
            yield c
words = (c + c for c in chargen())  #если нужно задать генератор, то рисуем круглые скобки

print('\nЗадание 3')
import time
from datetime import datetime
class TimeContextMenager:

    def __enter__(self):
        self.now1 = datetime.now()
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Время выполнения кода {} секунд.".format(datetime.now() - self.now1))
        return True
with TimeContextMenager():
    time.sleep(4)  # для красоты

print("\nЗадание 4")
import itertools
def threeone(m1, m2, m3):
    return itertools.chain(m1, m2, m3)
print(list(threeone([1, 2, 3], [4, 5], [6, 7])))

def mit(slovo):
    return itertools.combinations_with_replacement(slovo, 4)
print(list(mit('password')))

