def compare(a, b):
    print (str(a)) if a > b else print (str(b))

def compare2(a, b):
    return a if a > b else b

print (str(compare2(3, 4)))
print (str(compare2(5, 2)))
compare(7, 8)
compare(9, 10)

