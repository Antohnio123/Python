
import heapq

arr = [0,3,24,2,3,7]

position_in_arr = 0

while arr != [0,2,3,3,7,24]:

    if position_in_arr ==0:
        larg = heapq.nsmallest(1, arr)

    else:
        larg = heapq.nsmallest(position_in_arr+1, arr)

    min_larg = (larg[position_in_arr])

    min_index = arr.index(min_larg)

    arr[position_in_arr], arr[min_index] = arr[min_index], arr[position_in_arr]

    position_in_arr += 1
    
else:
     print(arr)


