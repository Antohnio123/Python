def to_title(a) :
    if type(a) is not str :
        print("Argument type error")
        return []
    n=len(a)
    if n == 0 :
        return []
    if n == 1 :
        a = a[0].upper()
        return a
    i = 1
    a = a[0].upper() + a[1:n]
    while i < n :
        if a[i-1] == ' ' and a[i] == a[i].lower() :
            a=a[0:i] +a[i].upper() +a[i+1 :n]
        i= i+1
    return a

s = '   иван    петрович иванов   '
print('*',to_title(s),'*')