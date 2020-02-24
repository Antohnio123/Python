print()
print("*********************** Задача 3.2")
print()

import pickle

with open('human.data', 'rb') as f:
    data_new = pickle.load(f)

print(type(data_new))
print(data_new)
