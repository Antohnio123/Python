def multiplier(m=1, source=[4, 5, 6]):
    for i, x in enumerate(source):
        source[i] *= m

    return source


print(multiplier(5))
