for i in range(1,101):
    if i / 15 == i // 15:
        print('FizzBuzz')
    elif i / 5 == i // 5:
        print('Buzz')
    elif i / 3 == i // 3:
        print('Fizz')
    else:
        print(str(i))
