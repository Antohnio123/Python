import itertools

# Функция принимает три массива,а возвращает один

list_1 = [1,2,3]
list_2 = [4,5]
list_3 = [6,7]

my_list = list(itertools.chain(list_1,list_2,list_3))
print(my_list)

# Функция принимает лист из слов и выводит нам только те,которые имеют больше 5 букв

drop_list = ["hello", "i", "write", "cool", "code"]
data = list(itertools.filterfalse(lambda x: len(x)<5,drop_list))
print(data)

# Функция выводит разные комбинации источника

for item in itertools.permutations("password",8):
    print(" ".join(item))
