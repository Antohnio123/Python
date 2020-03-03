import time
import threading
import multiprocessing

def find_primes(end , st) :
    a = list(range(end+1))
    a[1] = 0
    lst = []
    i = 2
    while i <= end :
        if a[i] != 0 :
            if a[i] >= st :
                lst.append(a[i])
            for j in range(i, end +1, i): a[j] = 0
        i += 1
    return lst


a_end = [10000, 20000, 30000]
a_st = [3, 10001, 20001]

st_thr = time.time()
for i in range(3) :
    print (len(find_primes(a_end[i],a_st[i])),"Функция  ", i)
print (" Время последовательных вычислений : ", time.time() - st_thr)

st_thr = time.time()
threads= []
for n in range(3) :
    print("Поток ", n, 'Стартовал', time.time())
    thr = threading.Thread(target= find_primes, args = (a_end[n],a_st[n]))
    thr.start()
    threads.append(thr)
    thr.join()
print (" Время многопоточных вычислений : ", time.time() - st_thr)
print(threads)
if __name__ == '__main__':
    start_process = time.time()
    process = []
    for i in range (3) :
        print("Процесс ", i, "Стартовал ", time.time())
        p = multiprocessing.Process(target = find_primes, args = (a_end[i], a_st[i]))
        print(p)
        p.start()
        process.append(p)
        p.join()
        print(process)
    print ("Время многопроцессных вычислений ", time.time() - start_process)
    print(process)

