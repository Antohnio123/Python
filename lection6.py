import calendar
print(calendar.TextCalendar().formatyear(theyear=2020))
input()
exit()

import os

class WithTest():
    def __enter__(self):
        print("File opened!")
        self.f = open("Lec3_Tasks.txt", "a",encoding='utf-8')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Finish use with {} {} {}".format(exc_type, exc_val, exc_tb))
        self.f.close()

#with open("Lec3_Tasks.txt", "a",encoding='utf-8') as f:
#     f.write("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

with WithTest() as wt:
    print(type(wt))
    wt.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

exit()
#####################################
l = [1, 2, 3, 4]
mygen = (x*x for x in l)

#print(l)
#for i in l:
#    print(i)

print(next(mygen))
j = 0
for i in mygen:
    j += 1
    print(i)

print (j)

exit()
#############################################
import datetime
import time
import random

def gen():
    while True:
        str = datetime.datetime.now()
        randTime = random.randint(0, 5)
        print(randTime)
        time.sleep(randTime)
        yield str


g  = gen()

for i in g:
    print(i)

exit()
###########################################
l = [1, 2, 3, 4]
li = iter(l)
print(li)
input()
print(next(li))
input()
print(next(li))
input()
print(next(li))
input()

###########################################
filenames = ["mytext.txt", "cv.doc", "myphoto.jpg"]

i = 0
for f in filenames:
    print("reading file {} - {}".format(i, f))
    i+=1

for i, fname in enumerate(filenames, start=0):
    print("reading file {} - {}".format(i, fname))

###########################################
import hashlib

m = hashlib.sha256()
m.update(b"Some string")
print(m.hexdigest())
