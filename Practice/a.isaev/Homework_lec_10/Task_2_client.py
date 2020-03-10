
import socket
import random

class User:
    def __init__(self):
        pass

    def print_user_data(self):
        names = ["Niko", "Lena", "Kolya", "Masha", "Boris"]
        last_names = ["Bellic", "Franko", "Drons", "Hammes", "Mirell"]
        addreses = ["New York", "Dallas", "London", "Ivanovo", "Minsk"]
        name = random.choice(names)
        last_name = random.choice(last_names)
        addres = random.choice(addreses)
        return "{} {} from {}".format(name, last_name, addres).encode()

user_dada = User()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 9090
s.connect((host, port))
s.send(user_dada.print_user_data())
s.close()
