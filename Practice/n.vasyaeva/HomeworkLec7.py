print("Задача 1")
import datetime
import subprocess
import random
import pickle
def job(x1=2020, y1=1, z1=1, x2=2020, y2=2, z2=4):
    data_one = datetime.date(year=x1, month=y1, day=z1) #начало периода
    delta = datetime.timedelta(days=1)
    data_x = data_one + delta
    data_two = datetime.date(year=x2, month=y2, day=z2) #конец периода
    y = 0
    while data_x < data_two:
        if data_x.isoweekday() < 6:
            y += 1
        data_x = data_x + delta
    return print("Колличество рабочих дней - ", y)
job()

print("\nЗадача 3")
class Human():

    def __init__(self):
        self.first_name = random.choice(["Bill", "John",  "Harry", "William"])
        self.last_name = random.choice(["A", "B", "C", "D"])
        self.age = random.choice([22, 31, 45, 39])
        self.address = random.choice(["N.Novgorod", "Moscow", "New York", "Houston"])
        self.profession = random.choice(["engineer", "teacher", "developer"])

def create(numbe):
    n = 1
    spisok = []
    while n <= numbe:
        data = Human()
        spisok.extend([data.first_name, data.last_name, data.age, data.address, data.profession])
        n += 1
    f = open('human.data', 'wb')
    pickle.dump(spisok, f)
    f.close()

create(int(input("Enter the number of employees: " )))

def ch():
    f = open('human.data', 'rb')
    print(pickle.load(f))
    f.close()
ch()


print("\nЗадача 2  :((")
#def chit(command = "cmd.exe"):
 #   proc = subprocess.call(command) #, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
 #   f = proc.communicate('type c:\\Users\\Natalia\\PycharmProjects\\lec7\\forhw7.txt')
  #  return
#chit()
