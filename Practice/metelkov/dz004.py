
# vivod na ekran ot 1 do 100, esli kratno 3 - element = Fizz, esli kratno 5 element = Buzz
# esli kratno 15 element = FizzBuzz
a = []                      #sozdal spisok
for i in range(1,101):      #dobavil ot 1 do 100 - VNIMANIE na diapazon
    a.append(i)             #dobavlenie v spisok
for j in range(len(a)+1):   #perebor spiska po dline VNIMANIE na diapazon
    if j % 3 == 0:          #proverka kratno 3
        a[j-1] = 'Fizz'     #podmena elementa VNIMANIE na diapazon
    if j % 5 == 0:
        a[j - 1] = 'Buzz'
    if j % 15 == 0:
        a[j - 1] = 'FizzBuzz'
print(a)                    #vivod izmenennogo spiska

#---------------------------------------------------------------

# vvesti pyatgiznachnoe chislo i vivesti kazhduyu cifru v otdel stroke p=43209
# 1 cifra = 4
# 2 cifra = 3
# 3 cifra = 3   i t.d.
test = 1                                    #dlya beskonechnogo while
while test < 10:                            #zapusk beskonechnogo cikla
    vvod = input("INPUT 5 INT DIGIT :")     #vvod simvolov
    if len(vvod) != 5:                      #proverka - d.b. tolko 5 simvolov
        print('YOU NEED INPUT ONLY 5 DIGIT') #prosit vvesti tolko 5, esli v vvode oshibka
    else:
        break                               #vihod is cikla kogda vvedeno 5 simvolov

for o in range(len(vvod)):                  #perebor 5 strok
    print(str(o+1) + " DIGIT IS " + str(vvod[o]))  # vivod strok
# ne realizovana proverka na ne cifri n znaki

#-----------------------------------------------------------------------

#sortirovka viborom - otsortirovat massiv
arr = [0, 3, 24, 2, 3, 7]
print("dan massiv: " + str(arr))
#neverniy var
arr.sort()
print("sorted: " + str(arr))
print('--------------')

def swap(a, b):
    #a, b = b, a
    #prom = ''
    #prom = b
    #b = a
    #a = prom
    return b, a

dlin = len(arr)
massnew = []
promezhmass = []
for i in range(dlin - 1):
    min = i
    for j in range(i + 1, dlin - 1):
        if a[j] < a[min]:
            min = j
        if min != i:
            #a, b = b, a
            swap(a[i], a[min])
            #a[i], a[min] = a[min], a[i]
    print("ddd")
