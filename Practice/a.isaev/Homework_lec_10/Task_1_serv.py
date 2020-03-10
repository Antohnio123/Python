import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.bind(("localhost",9090))
my_sock.listen(1)
conn, addr = my_sock.accept()
print("Connected: ", addr)
words = {"cat" : "myau", "cow" : "muu", "human" : "lalala"}
while True:
    data = conn.recv(1024)
    data = data.decode()
    gett = words.get(data)
    conn.send(gett.encode())
    if not data:
        break
print("Connection lost")
conn.close()