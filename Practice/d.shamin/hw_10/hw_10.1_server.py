import threading
import socket
import pickle

d = {'cold': "ice", 'red': "button", "lang": "python"}


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr

    def run(self):
        ans = []
        print('Соединяюсь с {}'.format(self._address))
        data = self._connection.recv(1024)
        print('Получено: {}'.format(data.decode()))
        self._connection.send(data)
        wrd = self._connection.recv(1024)
        for i in pickle.loads(wrd):
            ans.append(d.get(i))
        self._connection.send(pickle.dumps(ans))
        self._connection.close()
        print('Закрыто соединение с {}'.format(self._address))
        print()


class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._runnning = False

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._runnning = True
        print('Сервер запущен...')
        print()
        while self._runnning:
            conn, addr = self._socket.accept()
            ClientThread(conn, addr).start()

    def stop(self):
        self._runnning = False
        self._socket.close()
        print('Сервер остановлен')


if __name__ == '__main__':
    srv = TcpServer(host='192.168.1.21', port=5555)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()
