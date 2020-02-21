# Ошибка была в том,что мы присваиваем источник к результату,тем самым изменяя исходные данные.
# Реализовать можно несколькими способами :
# 1) Через пустой список и добавление в него результата
# 2) Через enumerate

def multiplier(m=1, source=[1, 2, 3]):
    result = []
    for i in source:
        i *= m
        result.append(i)

    return result

my_source = [1,2,3,4,5]
print(multiplier(10, b))
print(b)
