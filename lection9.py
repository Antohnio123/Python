from multiprocessing import Pool
def cube(x):
    return x**3

if __name__ == '__main__':
    pool = Pool(processes=4)
    res = pool.map(cube, range(1,7))
    print(res)

exit()

from multiprocessing import Process, Pipe

def f(conn):
    conn.send(['hello', 11, None])
    #print('Client receives: {}'.format(conn.recv()))

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()

    p = Process(target=f, args=(child_conn,))
    p.start()

    print('Server receives: {}'.format(parent_conn.recv()))
    #child_conn.send(['python', 3])
    p.join()

exit()

from threading import Thread
import time
import multiprocessing

def count(n):
    while n > 0:
        n -= 1

c = 80000000

if __name__ == '__main__': # обязательно для многопроцессного приложения
    start = time.time()
    p1 = multiprocessing.Process(target=count, args=(c,))
    p2 = multiprocessing.Process(target=count, args=(c,))
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
