def compare (a, b, c):
    if a>=b and b>=c:
        print ("Самое большое число - " + str(a) + ", затем " + str(b) + ", самое низкое - " + str(c))
    elif b>=a and a>=c:
        print ("Самое большое число - " + str(b) + ", затем " + str(a) + ", самое низкое - " + str(c))
    elif c>=b and b>=a:
        print ("Самое большое число - " + str(c) + ", затем " + str(b) + ", самое низкое - " + str(a))
    elif a>=c and c>=b:
        print ("Самое большое число - " + str(a) + ", затем " + str(c) + ", самое низкое - " + str(b))
    elif b>=c and c>=a:
        print ("Самое большое число - " + str(b) + ", затем " + str(c) + ", самое низкое - " + str(a))
    else :
        print ("Самое большое число - " + str(c) + ", затем " + str(a) + ", самое низкое - " + str(b))

print ("Введите первое число")
a = input()

print ("Введите второе число")
b = input()

print ("Введите третье число")
c = input()

compare (a,b,c)

print ("Введите любой знак чтобы выйти")
input() 

