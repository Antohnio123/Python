import threading
def sum_any_types(*args):
    r = None
    if type(args[0]) is int: n = 0
    if type(args[0]) is str: n = ''
    if type(args[0]) is list: n = []
    for arg in args: n += arg
    print(n)
    return n

type_int = 1, 2, 3, 4, 5, 6, 7, 8, 9
type_str = 'Тип ','слагаемых ','данных ','зто ','строка ','!!'
type_list = ["Тип ","слагаемых ","данных "],["это","лист"],["!!","!!"]

threads = []
for data in type_int, type_str, type_list :
    thr = threading.Thread(target=sum_any_types, args=data)
    thr.start()
    threads.append(thr)
for thr in threads: thr.join()
