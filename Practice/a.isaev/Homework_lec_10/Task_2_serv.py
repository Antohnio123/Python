import socket



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 9090
s.bind((host, port))
s.listen(3)
conn, addr = s.accept()
print("User {} connected".format(addr))
tick = 0
while tick != 3:
    conn, addr = s.accept()
    data = conn.recv(1024)
    print(data.decode())
    tick += 1





