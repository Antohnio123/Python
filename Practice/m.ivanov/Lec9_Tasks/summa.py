import time
import multiprocessing


def timer(func): # декоратор для подсчёта времени работы функции
    def tmp(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        time.sleep(3)
        print("Spent: {} seconds".format(time.time()-t))
        return res
    return tmp


def summa(a, b):
    print(a + b)


@timer
def summa_single():
    for a, b in zip(arr_1, arr_2):
        summa(a, b)


@timer
def summa_multi():
    proc = []
    for a, b in zip(arr_1, arr_2):
        p = multiprocessing.Process(target=summa, args=(a, b))
        p.start()
        proc.append(p)
    for p in proc:
        p.join()


arr_1 = [1, [1], '1']
arr_2 = [2, [2], '2']


if __name__ == '__main__':
    print('Single:')
    summa_single()
    print('Multi:')
    summa_multi()
