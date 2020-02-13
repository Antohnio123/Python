from random import randint


n = int(input('Enter array length: '))
arr=[]
for i in range(n):
    arr.append(randint(1, 99))
print(arr)

#вариант не полностью соответствующий условиям задания. элементы не меняются местами, а переносятся в соответствующий интервал
# for i in range(n):
#     arr.insert(i, arr.pop(arr.index(min(arr[i:]))))
# print(arr)

for i in range(n):
    m = (arr[i:].index(min(arr[i:]))) + i
    arr[i], arr[m] = arr[m], arr[i]
print(arr)