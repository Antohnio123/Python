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


a_time = time.time()

strt = 3
fin = 10000
find_primes(fin, strt)

strt = 10001
fin = 20000
find_primes(fin, strt)

strt = 20001
fin = 30000
find_primes(fin, strt)

b_time = time.time() - a_time
print(b_time)

