for a in range(1,101): # cоздаем список
    if (a%15)==0: #каждое кратное число переименоваем на FizzBuzz
        print("FizzBuzz")
    elif (a%3)==0:  # кратное 3 меняем на Fizz
        print("Fizz")
    elif (a%5)==0: # кждае кратное 5 переменовать в Buzz
        print("Buzz")
    else:
        print(a) # Вывести результат