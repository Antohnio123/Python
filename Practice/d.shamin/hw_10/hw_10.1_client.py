import socket
import random
import pickle

class TcpClient:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self._socket = None

    def run(self, lst):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        self._socket.send(self.name.encode())
        data = self._socket.recv(1024)
        print('Получено: {}'.format(data.decode()))
        self._socket.send(pickle.dumps(lst))
        ans = self._socket.recv(1024)
        print(pickle.loads(ans))
        self._socket.close()


lst = ["red", "lang", "cold"]

if __name__ == '__main__':
    name = 'Клиент ' + str(random.randint(1, 1000))
    myclient = TcpClient(host='192.168.1.21', port=5555, name=name)
    myclient.run(lst)
