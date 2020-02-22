# def multiplier(m = 1, source = [1, 2, 3]):
#     result = source
#     for i, e in enumerate(source):
#         result[i] *= m
#     return result
# Mistakes:
# 1. Mutable Default Argument
# print(multiplier(3))
# [3, 6, 9]
# print(multiplier(5))
# [18, 36, 54]
# 2. Maybe? multiplier([1, 2]) = [1,2], [1,2,1,2], [1,2,1,2,1,2]


def multiplier(source = None, m = 1):
    if source is None:
        source = [1, 2, 3]
    result = list(map(lambda x: x*m, source))
    return result

print(multiplier(None, 3))
print(multiplier(None, 5))
print(multiplier([2, 4, 6, 8], 2))
print(multiplier([2,3,4]))
#print(multiplier(2))


