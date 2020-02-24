def multiplier2 (m=1, source=[1,2,3]):
    result = source
    for i,x in enumerate(source): # зачем использовать enumerate,если мы не обходим последовательность
        result[i] *= m
    return result
print(multiplier2 (5))
print(multiplier2 (12, [1,2]))
#################################
