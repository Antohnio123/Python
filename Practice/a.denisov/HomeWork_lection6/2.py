def multiplier(m=1, source=(1, 2, 3)):
    result = list(source)
    for i, x in enumerate(result):
        result[i] *= m

    return result


print(multiplier())
print(multiplier())
print(multiplier())
print(multiplier(2, [3, 5, 7]))
print(multiplier())
print(multiplier(4))
