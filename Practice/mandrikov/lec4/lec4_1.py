a = list(range(100))
for i in range(1, 100):
    if a[i] % 15 == 0:
        a[i] = 'FizzBuzz'
    elif a[i] % 5 == 0:
        a[i] = 'Buzz'
    elif a[i] % 3 == 0:
        a[i] = 'Fizz'
print(a)
