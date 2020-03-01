
a = [1,2,3,"4Петя",5,"6Коля"]
def Reversed (source) :
    z=int(len(source)/2)
    m=len(source)-1
    for i in range(0,z) :
        source[i],source[m-i] = source[m-i],source[i]
    return source
print(Reversed(a))
print(a)



