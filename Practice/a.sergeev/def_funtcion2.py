def compare (a, b, c):
    if a>=b and b>=c:
        print ("Samoe bolsho chislo " + str(a) + ", potom " + str(b) + ", potom " + str(c))
    elif b>=a and a>=c:
        print ("Samoe bolsho chislo " + str(b) + ", potom " + str(a) + ", potom " + str(c))
    elif c>=b and b>=a:
        print ("Samoe bolsho chislo " + str(c) + ", potom " + str(b) + ", potom " + str(a))
    elif a>=c and c>=b:
        print ("Samoe bolsho chislo " + str(a) + ", potom " + str(c) + ", potom " + str(b))
    elif b>=c and c>=a:
        print ("Samoe bolsho chislo " + str(b) + ", potom " + str(c) + ", potom " + str(a))
    else :
        print ("Samoe bolsho chislo " + str(c) + ", potom " + str(a) + ", potom " + str(b))

print ('Vvedite chislo x')
x = input()

print ('Vvedite chislo y')
y = input()

print ('Vvedite chislo z')
z = input()

compare (x,y,z)
