
import copy
def multiplier1 ( m= 1, source = [ 1, 2, 3]) :
    result = copy.copy(source)
    for i, x in enumerate(source) :
        result[i] = result[i] * m
    return result


def multiplier ( m= 1, source = [ 1, 2, 3]) :
    result = list(source)
    for i, x in enumerate(source) :
        result[i] = result[i] * m

    return result

a = [10, 10, 20, 50]
print(multiplier(5))
print(multiplier(12, [1, 2]))
print(multiplier(3, a))
print(a)
