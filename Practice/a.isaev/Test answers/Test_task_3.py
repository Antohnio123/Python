import math
def my_range(stop,start = 0, step = 1):
    result = []
    result.append(start)
    if isinstance(stop,int) and isinstance(start,int) and isinstance(step,int) == True:
        if step > 0:
            i = 1
            while i < stop:
                result.append(start + step * i)
                i += 1
                if stop == i * step + step:
                    break
                else:
                    continue
                return result
        else:
            i = -1
            while int(math.fabs(i)) < (stop + step) // step:
                result.append(start - step * i)
                i -= 1
            return result

    else:
        print('Please,input the numbers')

print(my_range(-10,2,-2))
