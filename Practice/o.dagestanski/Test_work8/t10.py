class Money():
    def __init__(self, wholes, cents):
        if type(wholes) != int:
            raise TypeError('Рубль должен быть целым числом')
        if cents not in range(0, 100):
            raise ValueError('Копейка должна быть числом от 0 до 99')
        self.wholes = int(wholes)
        self.cents = int(cents)
        self.sum = self.wholes * 100 + self.cents

    def __str__(self):
        return f'{self.wholes},{self.cents}'

    def __add__(self, other):
        new_wholes = self.wholes + other.wholes + ((self.cents + other.cents)//100)
        new_cents = (self.cents + other.cents) % 100
        return Money(new_wholes, new_cents)
    def __sub__(self, other):
        new_wholes = (self.sum - other.sum) // 100
        new_cents = (self.sum - other.sum) % 100
        return Money(new_wholes, new_cents)
    def __truediv__(self, other):
        new_wholes = (self.sum / other.sum) // 100
        new_cents = (self.sum / other.sum) % 100
        return Money(new_wholes, new_cents)
    def __lt__(self, other):
        if self.sum < other.sum :
            return True
        else :
            False
    def __le__(self, other):
        if self.sum <= other.sum :
            return True
        else :
            False
    def __eq__(self, other):
        if self.sum == other.sum :
            return True
        else :
            False
    def __ne__(self, other):
        if self.sum != other.sum :
            return True
        else :
            False
    def __gt__(self, other):
        if self.sum > other.sum :
            return True
        else :
            False
    def __ge__(self, other):
        if self.sum >= other.sum :
            return True
        else :
            False
    def getCourse(self, course):
        self.course = int(course)
        new_wholes = (int(self.sum/course))//100
        new_cents = (int(self.sum/course)) % 100

        return Money(new_wholes,new_cents)

bm_1 = Money(80, 98)
print(bm_1)
bm_2 = Money(2, 30)
print(bm_2)
bm_3 = bm_2 + bm_1
print(bm_3)
print(bm_1 - bm_2)
print(bm_1.getCourse(70))
