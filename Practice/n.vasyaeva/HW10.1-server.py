import socket
a = dict(one=1, two=2, three=3, four=4, five=5, six=6)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.13'
port = 12345
s.bind((host, port))
s.listen(1)
tran = []
while True:
    conn, addr = s.accept()
    print('Server got connection from {}'.format(addr))
    conn.send('Thank you for the connection'.encode())
    j =list(conn.recv(1024).decode().split(" "))
    x = 0
    while x < len(j):
        if j[x] in a:
            tran.append(a[j[x]])
        x+=1
    conn.send('Расшифрованные слова {}'.format(tran).encode())
    conn.close()
s.close()