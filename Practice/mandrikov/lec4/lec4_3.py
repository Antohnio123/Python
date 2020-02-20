arr = [0, 3, 24, 2, 3, 7]
for i in range(len(arr)):
    minimum = i
    for j in range(i + 1, len(arr)):
        if int(arr[j]) < int(arr[minimum]):
            minimum = j
    arr[i], arr[minimum] = arr[minimum], arr[i]
print(arr)
