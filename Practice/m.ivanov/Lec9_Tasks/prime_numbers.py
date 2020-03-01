import time
import threading
import multiprocessing





# Пусть будет для сравнения

def sieve_eratosphenes(n):
     a = [x for x in range(n + 1)]
     a[1] = 0
     result = []
     i = 2
     while i <= n:
         if a[i] != 0:
             result.append(a[i])
             for j in range(i, n+1, i):
                 a[j] = 0
         i += 1
     return result


def timer(func): # декоратор для подсчёта времени работы функции
    def tmp(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print("Spent: {} seconds".format(time.time()-t))
        return res
    return tmp


def prime_number(m, n): # функция нахождения простых чисел. не совсем правильная.
    if m % 2 == 0:
        m += 1
    result = []
    for i in range(m, n + 1, 2):
        j = 3
        while True:
            if i % j == 0:
                break
            if (j * j) > i:
                result.append(i)
                break
            j += 1
    return result

@timer
def prime_single():
    for a, b  in zip(begin, end):
        prime_number(a, b)


@timer
def prime_multithreads():
    threads = []
    for a, b  in zip(begin, end):
        thr = threading.Thread(target = prime_number, args = (a, b))
        thr.start()
        threads.append(thr)
    for thr in threads:
        thr.join()


@timer
def prime_multiproc():
    proc = []
    for a, b  in zip(begin, end):
       p = multiprocessing.Process(target=prime_number, args=(a, b))
       p.start()
       proc.append(p)
    for p in proc:
        p.join()

# number = int(input('Enter numbers of ranges: '))
# length = int(input('Enter length of range: ' ))

begin = [(x*10000) + 1 for x in range(0, 3)]
end = [(x*10000) for x in range(1,4)]


# Многопроцессность даёт выигрыш во времени при длине интервала > 12000 при 3 интервалах
# или при длине интервала 10000 при числе интервалов > 4
# При длине интервала 100000 и количестве 3: выигрыш в два раза
# Нормально реализованное решето Эратосфена даёт выигрыш в 10 раз на этом интервале
# Мультипоточность не даёт заметного выигрыша в скорости как при длинных, так и при коротких интервалах
# по сравнению с одним потоком. Но результат не чистый, так как второй и третий поток вынуждены искать
# делители в диапазоне [3, sqrt(begin)] и проверять делимость

if __name__ == '__main__': # обязательно для многопроцессного приложения
    print('One thread:')
    prime_single()
    print('Multithreads:')
    prime_multithreads()
    print('Multiprocesses:')
    prime_multiproc()
    print('Sieve of Eratosphenes:')
    sieve_eratosphenes = timer(sieve_eratosphenes)
    sieve_eratosphenes(end[2])




