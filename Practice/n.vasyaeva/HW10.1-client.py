import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.13'
port = 12345
s.connect((host, port))
d = s.recv(1024)
print(d.decode())
word = input("Введите через пробел какой-либо список из слов: one, two, three, four, five, six.")
s.send(word.encode())
f = s.recv(1024)
print(d.decode())
s.close()