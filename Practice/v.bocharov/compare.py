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

a = 69
b = 420
c = 1337
compare(a,b,c)
