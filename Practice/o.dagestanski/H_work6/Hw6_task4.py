
from itertools import chain
def CombineArrays (*args):
    return list(chain(*args))

a=CombineArrays([1,2,3],[4,5],[6,7])
print(a)

from itertools import filterfalse
def func(x):
    return len(x) < 5
def FilterSelection (*args) :
    z = filterfalse( func , [*args])
    return list(z)

b = FilterSelection("hello","i","write", "cool","code")
print(b)

from itertools import combinations
def CombinationsChars(s, l) :
    return list(combinations(s,l))
c = CombinationsChars("password", 4)
for i in c :
    print(i)

