sn = input("Введите массив чисел через пробел :").strip().split()
l_sn = len(sn)
for i in range(l_sn) :
    sn[i] = int(sn[i])
print("       Исходный массив :",sn)
for i in range(0,l_sn) :
    min_i = i
    i_st = i + 1
    for i1 in range(i_st,l_sn) :
        if sn[i1] < sn[min_i] :
            min_i = i1
    sn[i], sn[min_i] = sn[min_i], sn[i]

print("Отсортированный массив :",sn)
