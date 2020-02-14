#думаю, это делается не так)

def tabtospaces(filename, n):#замена табуляции на пробелы
    file = open(filename, 'r')
    data = file.read()
    file.close()
    file = open(filename, 'w')
    file.write(data.expandtabs(tabsize = n))
    file.close()

def spacestotab(filename, n):#замена пробелов на табуляцию
    file = open(filename, 'r')
    data = file.read()
    file.close()
    file = open(filename, 'w')
    file.write(data.replace(' ' * n,'   '))
    file.close()