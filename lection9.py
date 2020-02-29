
from threading import Thread
import time
import multiprocessing

def count(n):
    while n > 0:
        n -= 1

c = 80000000

if __name__ == '__main__': # обязательно для многопроцессного приложения
    # c = 80000000
    start = time.time()
    p1 = multiprocessing.Process(target=count,args=(c,))
    p2 = multiprocessing.Process(target=count,args=(c,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('{0:3.2f} sec.'.format(time.time() - start))

    start = time.time()
    count(c)
    count(c)
    print('{0:.2f} sec.'.format(time.time() - start))

    start = time.time()
    t1 = Thread(target=count, args=(c,))
    t2 = Thread(target=count, args=(c,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('{0:.2f} sec.'.format(time.time() - start))
    exit()

#############################

import threading
import time

def t1(x, event):
    print("Начинаю работать!")
    time.sleep(5)
    event.set()
    pass

def t2(x, event):
    print("Жду!")
    event.wait()
    event.clear()
    print("Дождался!")
    pass


event = threading.Event()

tr1 = threading.Thread(name="server", target=t1, args=(0 ,event))
tr1.start()

tr2 = threading.Thread(name="client", target=t2, args=(1 ,event))
tr2.start()


tr1.join()
tr2.join()
