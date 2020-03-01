# Практика. Задание 1

def my_len(list):
    length = 0
    for _ in list:
        length += 1
    print(length)


a = [1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 5]
my_len(a)


# Практика. Задание 2

def my_reversed(list):
    length = len(list)
    position = length - 1
    zero_position = 0
    while position != zero_position:
        list[zero_position], list[position] = list[position], list[zero_position]
        zero_position += 1
        position -= 1
    print(list)


my_reversed(a)

# Практика. Задание 4

my_string = "isaev alexander sergeevich"


#def to_title(str):
#    splitted = my_string.split()
#    length = len(splitted)
#    num = 0
#    while num != length-1:
#       splitted[num].capitalize()
#        num + 1
#    str.join()
#    print(str)


#to_title(my_string)
