from urllib import request
req = request.Request('http://www.ya.ru')
response = request.urlopen(req)
web_page = response.read()
print(web_page)

exit()
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.254.48'
port = 12345
s.connect((host, port))
# подключаемся к серверу
d = s.recv(1024)
# получаем данные от сервера (1024 байта - размер буфера для данных)
# преобразуем данные из байтового представления в строковое и выводим
# (преобразование из utf-8 в ascii)
print(d.decode())
s.close()

exit()

import threading
import queue
import time
import keyboard

q = queue.Queue()
#

def private_cube():
    char = ""
    while True:
        try:
            char = q.get_nowait()
        except queue.Empty:
            pass
        if (char != ""):
            print(char)
            time.sleep(1)


thr = threading.Thread(target=private_cube)
thr.start()

while True:
    char = input()
    if char == 'q':
        break
    q.put(char)

thr.join()