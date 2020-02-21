
def chargen() :
#    while True :
        for c in list("0123456789") :
            yield c

words = [c + c for c in  chargen()] #[:10]
print(words)
