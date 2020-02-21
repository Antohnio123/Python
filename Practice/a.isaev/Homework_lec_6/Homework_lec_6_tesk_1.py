# Ошибка была в квардратных скобках итератора words

def chargen():
    while True:
        for c in '0123456789':
            yield c


words = (c + c for c in chargen())
print(next(words))
print(next(words))
print(next(words))
print(next(words))
print(next(words))

