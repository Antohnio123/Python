import random
import pickle

class Human():
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place


def create_and_serialise(n, name, min_age, max_age, place):
    data = []
    for i in range(n):
        h_name = random.choice(name)
        h_age = random.randint(min_age,max_age)
        h_place = random.choice(place)
        h = Human(h_name, h_age, h_place)
        data.append(h)
    with open("human.data", "wb") as file:
        pickle.dump(data, file)

def deserialise():
    with open('human.data', 'rb') as file:
         data_new = pickle.load(file)
    return data_new

n = int(input('Enter number of humans: '))
list_of_names = input('Enter names for human thru space: ').split()
list_of_places = input('Enter places for human thru space: ').split()
min_age = int(input('Enter minimum age for human: '))
max_age = int(input('Enter maximum age for human: '))


create_and_serialise(n, list_of_names, min_age, max_age, list_of_places)
print(deserialise())



