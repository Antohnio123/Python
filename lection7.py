import itertools
def comp(x):
    return len(x)==5

def length_control(*args: str, length=5):
    print (args) # вот тут видно, что пришло в args и почему не работало с [*args]
    return list(itertools.filterfalse(lambda x: len(x) < length, args[0]))

def length_control1(*args: str, length=5):
    return list(itertools.filterfalse(comp, [*args]))


l =  ['hello', 'i', 'write', 'cool', 'code']
print(length_control(l))

exit()
#########################################
import os
#print(os.path.dirname("C:\\Users\\a.anikin\\PycharmProjects\\hey\\Lec3_Tasks.txt"))
#print(os.path.basename("C:\\Users\\a.anikin\\PycharmProjects\\hey\\Lec3_Tasks.txt"))
oldpath = os.getcwd()
print(os.chdir("c:\\"))

print(os.getcwd())
print(os.path.exists("Lec3_Tasks.txt"))

os.chdir(oldpath)
print(os.getcwd())
print(os.path.exists("Lec3_Tasks.txt"))

exit()
##################################
import sys

print(sys.flags.debug)

exit()

###################################
import random
l = ["камень", "ножницы", "бумага" ]
#for i in range(10):
    #random.shuffle(l)
    #print(l)

print(random.choice(l))

exit()

#########################
import datetime
dt =  datetime.datetime(2019, 7, 27, 13, 12, 54, 334243)
print (dt.weekday())
dt1 =  datetime.datetime.now()
print (dt1.weekday())

exit()
###########################################
import os

def gen():
    seek = 0
    with open("inflammation-01.csv", "r", encoding='utf-8') as file:
        file.seek(seek)
        str = file.readline()
        while str:
            yield str
            str = file.readline()


g  = gen()
print(next(g))
input()
#for i in g:
#    print(i)
print(next(g))
input()
print(next(g))

exit(0)
###################################
def multiplier2 (m=1, source=[1,2,3]):
    result = [x for x in source]
    for i in range(len(source)):
        result[i] = m * source[i]
        #result.append(m * i)
    return result

l = [3,5,6]
print(l)

#print(multiplier2 (5))
print(multiplier2 (12, l))

print(l)


exit()
########################################
import time
def chargen():
   while True:
        for c in '0123456789':
            yield c

words = (c for c in chargen())

while True:
    print(next(words))


exit()
########################################
