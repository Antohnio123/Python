import itertools


def mychain(*lists):
   return list(itertools.chain(*lists))

# def longwords_without_itertools(lst = None, n = 5): #Не могу понять как, используя itertools, сделать так,
#     if lst is None:                                 #чтобы на вход функции поступал массив
#         lst =['Hello', 'I', 'write', 'cod']         #nаким способом как в заккоментированном примере
#     return [word for word in lst if len(word) >= n]
#
# lst = ['aaaaa', 'aa', 'aaaaaa']
# print(longwords_without_itertools(lst))

def longwords(*words, n=5):
    return list(itertools.filterfalse(lambda word: len(word) < n, [*words]))

def combination(str, n=5):
    return list(itertools.combinations(str, n))

print(mychain([1, 2, 3], [4, 5], [6, 7]))
print(combination('password', 5))
print(longwords('hello', 'i', 'write', 'code'))




