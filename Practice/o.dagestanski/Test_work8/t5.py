def count_symbol (s : str, c :str) -> int :
    if len(s) == 0 or len(c) == 0 or len(c) > 1 :
        print("Argument error")
        return 0
    i = 0
    m = len(s)
    j = 0
    while i < m :
        if s[i] == c :
            j += 1
        i += 1
    return j

print(count_symbol("Hi, Elvis, I am here!iii ","i"))
