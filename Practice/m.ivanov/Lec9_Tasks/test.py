import threading
import concurrent.futures

def cube(number):
    print(threading.currentThread().getName() + ' said: cube of the number {} is {}'.format(number, number ** 3))


numbers = range(0,10)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(cube, numbers)



