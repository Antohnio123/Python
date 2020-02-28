
class User :
    def __init__(self, name , age) :
        self.name = name
        self.age = age
    def setName(self, name) :
        self.name = name
    def getName(self) :
        return self.name
    def setAge(self, age) :
        self.age = age
    def getAge(self) :
        return self.age

class Worker (User):
    def __init__(self, name, age, salary) :
        self.salary = salary
        super().__init__(name, age)
    def setSalary(self, salary):
        self.salaru = salary
    def getSalaru(self):
        return self.salary

john = Worker('John', 25, 1000)
jack = Worker("Jack", 26, 2000)
print ("Сумма зарплат :", john.getSalaru()+jack.getSalaru())
