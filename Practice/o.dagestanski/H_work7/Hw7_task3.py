import random
import pickle

class Human :
    def __init__(self):
        l_name = ["Иван","Петр","Федор","Катя","Таня"]
        l_place =["Москва","Нижний Новгород","Владимир","Казань","Самара"]
        self.name = random.choice(l_name)
        self.age = random.randint(18,30)
        self.place = random.choice(l_place)
    def print_human(self):
        print(" Имя: {} , Возраст: {} , Место жительства: {} ".format(self.name,self.age,self.place))

def s (n=5):
    a=[]
    print("Загружены в human.data :")
    for i in range(n) :
        h=Human()
        a.append(h)
        h.print_human()
    with open("human.data", "wb") as file:
        pickle.dump(a, file)
    return

def d_s():
    try :
        with open("human.data", "rb") as file:
            ads = pickle.load(file)
        print("Выгружены из human.data :")
        for i in ads :
            i.print_human()
        content = '0'
    except IOError:
        content = "File does not exist."
    return content

n = int(input("Введите количество людей для human.data: "))
s(n)
d_s()
