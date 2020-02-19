string = 'тут текст такой'
print(string)
b = string.replace(' ', 'qqq')
n = b.replace("qqq", '\t')
r = n.expandtabs(tabsize=4)
print(r)