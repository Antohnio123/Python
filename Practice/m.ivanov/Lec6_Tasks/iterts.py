import itertools


def mychain(*lists):
   return list(itertools.chain(*lists))

def longwords(*word, n=5):
    return list(itertools.filterfalse(lambda x: len(x) < n, [*word]))

def combination(str, n=5):
    return list(itertools.combinations(str, n))

print(mychain([1, 2, 3], [4, 5], [6, 7]))
print(combination('password', 5))
print(longwords('hello', 'i', 'write', 'code'))

