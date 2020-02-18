class ICantMyau(Exception):
    pass

class Animal(object):
    color = "None"

    def __init__(self, legs = 2, name = "animal"):
        self.legs = legs
        self.name = name

    def whoiam(self):
        print (str(self.legs) + "  "+ self.name)

    def _saysomething(self, text):
        print (text)

    @classmethod
    def print_color(cls):
        print(cls.color)


class Cat(Animal):
    def __init__(self):
        super(Cat, self).__init__(4, "cat")

    def myau(self):
        self._saysomething("myua!!!")

class Human(Animal):
    def __init__(self):
        self.name = "human"
        self.legs = 2

    def say_privet(self):
        self._saysomething("Hey!")

    def myau (self):
        raise ICantMyau

    def whoiam(self):
        print("Human!!!")
        super(Human, self).whoiam()


cat = Cat()
hu = Human()

animals = [cat, hu]
for animal in animals:
    try:
        animal.myau()
    except ICantMyau:
        print("I can't myau!")

Animal.print_color()

c = 4 - 4

a = 0



if a != -1:
    print(a)
else:
    print('Something goes wrong!')