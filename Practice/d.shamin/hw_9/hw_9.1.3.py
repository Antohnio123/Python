import multiprocessing
import time

def find_primes(end, start):
    lst = []
    for i in range(start, end + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    print(lst)

if __name__ == '__main__': # обязательно для многопроцессного приложения
    a_time = time.time()
    proc1 = multiprocessing.Process(name='proc1', target=find_primes, args=(10000, 3))
    proc2 = multiprocessing.Process(name='proc2', target=find_primes, args=(20000, 10001))
    proc3 = multiprocessing.Process(name='proc3', target=find_primes, args=(30000, 20001))

    proc1.start()
    proc2.start()
    proc3.start()

    proc1.join()
    proc2.join()
    proc3.join()

    b_time = time.time() - a_time
    print(b_time)