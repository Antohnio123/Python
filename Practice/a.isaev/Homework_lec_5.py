import time
import random
import os
import tempfile

# First task

class Man():
    def __init__(self,name):
        self.name = name

    def solve_task(self):
        return print("I'm not ready yet.")

# Second task

class Pupil(Man):
    def solve_task(self):
        sec = random.randint(3,6)
        time.sleep(sec)
        return print("I'm not ready yet.")

pup = Pupil("Nikolay")
m = Man("Jorah")
pup.solve_task()
m.solve_task()

# Third task
# Не понимаю из-за чего при записи,помимо значения записи,выводится None

class WrapStrToFile(object):
    def __init__(self):
        self.filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            file = open(self.filepath)
            data = file.read()
            file.close()
            return print(data)
        except:
           return "File doesn't exist"

    @content.setter
    def content(self,value):
        self.value = value
        file = open(self.filepath,"w")
        write = file.write(self.value)
        file.close()
        return write

    @content.deleter
    def content(self):
        os.remove(self.filepath)

wstf = WrapStrToFile()
print(wstf.content)
wstf.content = "Abraabracadabra"
print(wstf.content)
del wstf.content
print(wstf.content)


