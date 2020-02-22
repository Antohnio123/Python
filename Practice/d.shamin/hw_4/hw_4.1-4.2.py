#1. FizzBuzz

cnt = 1
while cnt <= 100:
    if cnt % 15 == 0:
        print("FizzBuzz")
    elif cnt % 3 == 0:
        print("Fizz")
    elif cnt % 5 == 0:
        print("Buzz")
    else:
        print(cnt)
    cnt += 1

print()


#2. Число: 10819
cnt = 1
number = input("Введи число: ")
if number.isdigit():
    for i in number:
        print(str(cnt) + "-я цифра равна " + i)
        cnt += 1
else:
    print("Это не число! ")
