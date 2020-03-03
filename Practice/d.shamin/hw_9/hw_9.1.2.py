import time
import threading


def find_primes(end, start):
    lst = []
    for i in range(start, end + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    print(lst)

a_time = time.time()
th1 = threading.Thread(name='th1', target=find_primes, args=(10000, 3))
th2 = threading.Thread(name='th2', target=find_primes, args=(20000, 10001))
th3 = threading.Thread(name='th3', target=find_primes, args=(30000, 20001))

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()

b_time = time.time() - a_time
print(b_time)
