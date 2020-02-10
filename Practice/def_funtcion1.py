def compare (a, b, c):
    if a>=b & b>=c:
        print ("Samoe bolsho chislo" + str(a) + ", potom " + str(b) + ", potom " + str(c))
    elif b>=a & a>=c:
        print ("Samoe bolsho chislo" + str(b) + ", potom " + str(a) + ", potom " + str(c))
    elif c>=b & b>=a:
        print ("Samoe bolsho chislo" + str(c) + ", potom " + str(b) + ", potom " + str(a))
    elif a>=c & c>=b:
        print ("Samoe bolsho chislo" + str(a) + ", potom " + str(c) + ", potom " + str(b))
    elif b>=c & c>=a:
        print ("Samoe bolsho chislo" + str(b) + ", potom " + str(c) + ", potom " + str(a))
    elif c>=a & a>=b:
        print ("Samoe bolsho chislo" + str(c) + ", potom " + str(a) + ", potom " + str(b))

x=100
y=55
z=123

compare (x,y,z)
