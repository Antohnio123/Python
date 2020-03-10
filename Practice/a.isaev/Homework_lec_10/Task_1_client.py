import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(("localhost",9090))
words = ["cow", "human", "cat"]
for word in words:
    my_sock.send(word.encode())
    data = my_sock.recv(1024)
    print(data)
my_sock.close()
