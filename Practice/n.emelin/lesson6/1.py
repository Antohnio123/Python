def chargen():
    #while True: - цикл while не дает выйти для вызова следующий yield
     for c in '0123456789':
        yield c
words = [c+c for c in chargen()]
print(str(words))