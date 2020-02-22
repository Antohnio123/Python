def chargen():
    i = 0
    while True:
        for c in '0123456789':
            i += 1
            print(c)
            yield c
        if i == 10:
            break
words = [c+c for c in chargen()][:10]

print()


def multiplier(m=1, source=[1, 2, 3]):
    global result
    result = source
    for i, x in enumerate(result):
        result[i] *= m
    print(result)
    return result


multiplier(5)
multiplier(23, result)


print()

from datetime import datetime
import time
# НЕПОНЯТНО КАК СДЕЛАТЬ БЕЗ "from"


class Timecount:
    def __enter__(self):
        self.start_time = datetime.now()
        time.sleep(2)
        return self.start_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        dur = datetime.now() - self.start_time
        print(dur)

with Timecount() as tc:
    print("Прошло времени :")

exit()

