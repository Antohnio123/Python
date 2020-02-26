def myformat(string, *args):
    if isinstance(string, str) or isinstance(string, args):
        print("Введённые аргументы не являются строками, передайте строки в функцию.")
        return(1)
    L = []
    for i in args:
        L.append(i)

    S=list(string)
    if "{" in S and "}" in S:
        Ind1 = 0
    else:
        print("Позиции аргументов в строке не заданы")
        return (1)
    while Ind1 != -1:
        Ind1 = S.index('{')
        Ind2 = S.index('}')





# s = "dfghdhsh {} jfsfjh {}  shgs {} hsg {}  hfdgdfg"
# print(s.format("AAAA", "BBBB", "CCCC", "DDDD"))
