import time
import threading
import multiprocessing


def find_primes(end, start=3):
    my_len = end - start
    numbers = []
    n = 1
    numbers.append(start)
    primes = []
    while len(numbers) - 1 != my_len:
        numbers.append(start + n)
        n += 1
    for i in numbers:
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            primes.append(i)
        elif i == 2 or i == 3 or i == 5 or i == 7:
            primes.append(i)
    print(primes)


start = time.time()
find_primes(10000)
find_primes(20000, 10001)
find_primes(30000, 20001)
print("{} sec".format(time.time() - start))

start_1 = time.time()

my_dif = {10000: 3, 20000: 10001, 30000: 20001}

for begin, end in  my_dif.items():
    thr = threading.Thread(target=find_primes(begin, end))
    thr.start()
    thr.join()

print("{} sec".format(time.time() - start_1))

start_2 = time.time()

if __name__ == '__main__':
    for begin, end in my_dif.items():
        proc = multiprocessing.Process(target= find_primes(begin, end))
        proc.start()
        proc.join()
    print("{} sec".format(time.time() - start_2))
