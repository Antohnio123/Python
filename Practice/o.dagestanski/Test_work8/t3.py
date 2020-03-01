
def Range(start=None,stop=None,step=1) :
    if start is None :
        return 0
    if stop is None :
        stop = start
        start = 0
    if type(start) is not int or type(stop) is not int or type(step) is not int  :
        print("Argument type error")
        return 0
    a=[]
    if step > 0 :
        while stop > start :
            a.append(start)
            start += step
    elif step < 0 :
        while stop < start :
            a.append(start)
            start += step
    return a

