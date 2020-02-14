#3. Реализовать алгоритм сортировки выбором.

arr = [12, 0, 3, 600, 24, 2, 3, 7, 43]
lng = len(arr)
new_arr = []

for k in range(lng):
    i = 0
    for j in arr:
        if min(arr) == j:
            arr.pop(i)
            new_arr.append(j)
            break
        i += 1

print(new_arr)
