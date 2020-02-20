import array

print("Дан массив:\narr = [0, 3, 24, 2, 3, 7].")
arr = [0, 3, 24, 2, 3, 7]
# print("Наименьший элемент в массиве:", min(arr))
# arr.sort()
# print(arr)

min_index = arr.index(min(arr))
x = arr[0]
arr[0] = arr[min_index]
arr[min_index] = x
print(arr)

