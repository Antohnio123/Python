import numpy as np
import datetime


first_day = datetime.date(2020, 2, 10)
last_day = datetime.date(2020, 2, 18)

days = np.busday_count(first_day, last_day)

print(days)


print()
print("*********************** Задача 2")
print()

import subprocess as sp

args = ["notepad.exe", input("Введи имя файла: ")]

code = sp.Popen(args, stdout=sp.PIPE)
code.wait()
res = code.communicate()
print(res)


print()
print("*********************** Задача 3.1")
print()


import pickle
import random

class Human:
    def __init__(self):
        self.name = random.choice(["Alan", "Ethan", "Robert", "John", "Jeremy"])
        self.lname = random.choice(["Brown", "Murray", "Curtis", "Clarkson", "Nickson"])
        self.age = random.randint(20, 40)
        self.city = random.choice(["Moscow", "Samara", "Tula", "Tokyo", "Berlin"])
        self.country = random.choice(["Japan", "Russia", "Germany", "England", "China"])


lst = []

def humgen():
    h = Human()
    lst.append([h.name, h.lname, h.age, h.city, h.country])

i = 0

while i < 3:
    humgen()
    i += 1

with open('human.data', 'wb') as f:
    pickle.dump(lst, f)

