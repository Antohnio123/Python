def chargen():
    while True:  #Ошибка — MemoryError
        for c in '0123456789': #Причина — бесконечный цикл While
            yield c  #Простейший способ исправить — убрать его.


def chargen_fix():
    for c in '0123456789':
        yield c


word = [c + c for c in chargen_fix()][:10]
print(word)

