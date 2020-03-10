import socket

def decoder(ss) :
    s=""
    for i in range(32,126): s += chr(i)
    for i in range(1040, 1107): s += chr(i)
    s1 = s[::-1]
    d={}
    for i in range(len(s)): d[s[i]] = s1[i]
    res=""
    for i in range(len(ss)):
        if d[ss[i]] is not None : res += d[ss[i]]
        else : res += ss[i]
    return res

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(5) # Открываем порт на сервере (не более 5 клиентов одновременно)
while True:
    conn, addr = s.accept()
    ask = conn.recv(1024)
    ask = ask.decode()
    ask = decoder(ask)
    print('Server got connection from {}'.format(addr),ask)
    # Преобразуем строку в набор байтов (ascii в utf-8) и отправляем
    conn.send(ask.encode())
    conn.close()
# s.close()