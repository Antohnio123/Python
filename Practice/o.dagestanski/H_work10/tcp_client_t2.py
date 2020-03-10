import socket
import random

def coder(ss) :
    s=""
    for i in range(32,126): s += chr(i)
    for i in range(1040, 1107): s += chr(i)
    s1 = s[::-1]
    d={}
    for i in range(len(s)): d[s1[i]] = s[i]
    res=""
    for i in range(len(ss)):
        if d[ss[i]] is not None : res += d[ss[i]]
        else : res += ss[i]
    return res

class User :
    def __init__(self):
        l_name = ["Иван","Петр","Федор","Катя","Таня"]
        self.name = random.choice(l_name)
        self.age = random.randint(18,30)
    def user_name(self):
        return self.name
    def user_age(self):
        return self.age

i=0
while i<5 :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    s.connect((host, port)) # подключаемся к серверу
    u = User()
    ask = "User: "+u.user_name()+" возраст: "+str(u.user_age())
    ask = coder(ask)
    #print("Отправляем на сервер: ",ask)
    s.send(ask.encode())
    d = s.recv(1024)
    print(" Server connection: ",d.decode())
    s.close()
    i+=1