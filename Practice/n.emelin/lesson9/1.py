import datetime
import threading
import multiprocessing

class Timer:
    t1=0
    def __enter__(self):
        self.t1=datetime.datetime.now()
    def __exit__(self, exc_type, exc_val, exc_tb):
        t2 = datetime.datetime.now()
        print("Время выполнения = "+str(t2-self.t1))

def find_primes(start,end): #### применяем решето Эратосфера
    numbers = list(range(start, end + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(start * number, end + 1, number):
                numbers[candidate - start] = 0
    a=(list(filter(lambda x: x != 0, numbers)))
    return f"{a}"

def prosto_potoki():
    print("Последовательно")
    with Timer():
        find_primes(3,10000)
        find_primes(10001,20000)
        find_primes(20001,30000)

def miltipocessing_potoki ():
    if __name__ == '__main__':
        print("Мультипроцесс")
        with Timer():
            t1 = multiprocessing.Process(target=find_primes, args=(3, 10000))
            t2 = multiprocessing.Process(target=find_primes, args=(10001, 20000))
            t3 = multiprocessing.Process(target=find_primes, args=(20001, 30000))
            t1.start()
            t2.start()
            t3.start()
            t1.join()
            t2.join()
            t3.join()
def Thread_potoki ():
    print("Многопоточно")
    with Timer():
        t1 = threading.Thread(target=find_primes, args=(3, 10000))
        t2 = threading.Thread(target=find_primes, args=(10001, 20000))
        t3 = threading.Thread(target=find_primes, args=(20001, 30000))
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()

if __name__ == '__main__':
    prosto_potoki()
    miltipocessing_potoki()
    Thread_potoki()