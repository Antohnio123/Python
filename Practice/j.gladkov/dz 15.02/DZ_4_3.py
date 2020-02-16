a = [0, 3, 24, 2, 3, 7]
i = 0
min = a[i]
max = a[i]
while i < len(a):
    if a[i] < min:
        min = a[i]
    if a[i] > max:
        max = a[i]
    i = i + 1
print ( min, max )
a = sorted(a)
print (a)
