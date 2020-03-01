##### 1
def my_len(b):
    i = 0
    for index in b:
        i += 1
    print(i)
b =[1, 3, 5, 6, 7]
my_len(b)
print()

##### 2
def my_reserve(a):
    rv_list=a[::-1]
    return rv_list
print(my_reserve([5,6,5,9]))
###3
def Range(start, stop, step):
    a = start
    b = step
    c = stop
    while a <= c:
        yield a
        a = a + b
        if b == 0:
            print('step = 0')
            break
g = Range(1, 16, 0)
for i in g:
    print(i)
#### 4
def to_title (strig):
    print(str.title(strig))
to_title(' jfsdjfls kjfsd sdflkjdfksjdfksd')
#### 5
def count_symbol(string,a):
    print(string.count(a))
count_symbol('sdsadewhgfjhrshfjkdhjskdh','d')
###### 6



######## 7

#######8


#######9
class User:
    name = ''
    age = 0
    def setname(self,name):
        self.name =name
    def getname(self):
        return self.name
    def setage(self,age):
        self.age = age
    def getage(self):
        return self.age
class Worker(User):
    salary = 0
    def setsalary(self,salary):
        self.salary =salary
    def getsalary(self):
        return self.salary
John = Worker
John.age = 25
John.salary = 1000
Jack = Worker
Jack.age = 26
Jack.salary = 2000
print(Jack.salary+John.salary)

