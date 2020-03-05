import random
import threading
def show_value(data):
    try: val = data.value
    except AttributeError: print(threading.current_thread().name,'No value yet')
    else: print(threading.current_thread().name,'value = ',val)
    return

def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)
    return

local_data = threading.local()
show_value(local_data)
local_data.value = 1000
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()
    t.join()