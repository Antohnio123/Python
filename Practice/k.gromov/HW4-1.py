for figure in range(1, 101):
    if figure % 15 == 0:
        print('BuzzFizz')
    elif figure % 5 == 0:
        print('Fizz')
    elif figure % 3 == 0:
        print('Buzz')
    else:
        print(figure)
