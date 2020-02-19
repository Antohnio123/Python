# Напомню задачу: в чем ошибка?
#
# def chargen():
#     while True:
#         for c in '0123456789':
#             yield c
#
#
# words = [c + c for c in chargen()][:10]
# print(words)
#
#  Предположу, что в зацкливании while. Думаю, можно обойтись и без него.
#  Либо изменить условие в зависимости от задачи.


def chargen():
    for c in '0123456789':
        yield c


words = [c + c for c in chargen()][:10]
print(words)
input()
