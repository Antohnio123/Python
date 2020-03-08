import socket
import random


class User:
    def __init__(self):
        names = ['John', 'Jack', 'Jim', 'Jared', 'Jason', 'Jasper']
        self.name = random.choice(names)
        self.age = random.randint(20, 40)

    def introduce(self):
        return ', '.join([self.name, str(self.age)])


class TcpClient:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self._socket = None
    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        self._socket.send(self.name.encode())
        data = self._socket.recv(1024)
        print(format(data.decode()))
        self._socket.close()

user = User()
if __name__ == '__main__':
    name = user.introduce()
    myclient = TcpClient(host='127.0.0.1', port=5555, name=name)
    myclient.run()





