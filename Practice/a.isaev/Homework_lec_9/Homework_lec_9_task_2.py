
import threading

def addition(*args):
    if isinstance(args[0], int):
        sum_int = 0
        for i in args:
            sum_int += i
        print(sum_int)

    if isinstance(args[0], str):
        sum_str = ""
        for i in args:
            sum_str += i
        print(sum_str)

    if isinstance(args[0], list):
        sum_list = []
        for i in args:
            sum_list += i
        print (sum_list)

lists = [2,435,646,3,2],[2424,24,77,8,5],[35,53]
strings = "fwfwf", "hyhy", "pipip"
ints = 5, 6, 7, 8

for additions in lists, strings, ints:
    ad_func_thread = threading.Thread(target=addition, args=additions)
    ad_func_thread.start()
    ad_func_thread.join()



