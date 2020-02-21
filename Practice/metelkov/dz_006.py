c = '0123456789'
def chargen():
     while True:
         #for c in '0123456789': 
         yield c#words = [c+c for c in chargen()][:10]
q = chargen()
words = (c+c)
for c in chargen(): 
    c1 = words[:10]
    print(c1)



#######################

def multiplier(m=1, source=(1, 2, 3)):
 result = list(source)
 for i, x in enumerate(result):
 result[i] *= m

 return result


print(multiplier())
print(multiplier(2, [3, 5, 7]))


 
