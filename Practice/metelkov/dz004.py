
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
    return b, a


					#nayti minimal element, v stroke, i pomestit ego
					#na pervoe mesto, pomenyav mestami s tekushim, potom
					#sravnit sled element so vsey strokoy n naimenshiy
					#pomestit vtorim, pomenyav mestami s tekushim
                    #algoritm podsmotrel tut:
					# https://www.youtube.com/watch?v=KZxP5JqtKKA
arr = [0, 3, 24, 2, 3, 7] 		#dan ne sortirovannoy massiv
print("dan massiv: " + str(arr)) 	#prosto vicodin massiv - pokazivaem original
#neverniy var
arr.sort() 			            	#vstroennaya funkciya sortirovki
print("sorted: " + str(arr))		#vivodim otsortirovanniy massiv
print('--------------') 		#razdelitel varianta

def swap(a, b): 			#sozdaem funkciyu obmena mestami
    return b, a 			#vozvrat znacheniy
dlin = len(arr) 			#opredelyaem dlinu massiva
#massnew = []				#ne ispolzoval
#promezhmass = []			#ne ispolzoval
for i in range(dlin - 1): 		#perebor pervogo elementa massiva do predposlednego
    min = i 				    #novaya peremenneya, minimalniy element = elementu massiva
    for j in range(i + 1, dlin - 1):   #perebor s posleduyushimi elementami do predposlednego
        if arr[j] < arr[min]:	   #sravnivaem tekushiy s kotorim vzyali v proshlom cikle
            min = j 		       #prisvaivaem novoe znachenie 'min' esli tekushiy menishe
            if min != i: 		   #esli pereberaemoe znachenie ne ravno znache iz pervogo
					               #cikla - s kotorim sravnivaem
                swap(arr[i], arr[min])      #menyaem elementy mestami
print(arr) 					                #vivodim otsortirovanniy massiv

#----------------------------------------------------


# otkrit fayl na chtenie i zamenit TAB na 4 space, a 4 space na TAB
fo = open("myfile.txt", "r")                        #otkryt file s imenem na chtenie
line = fo.readline()                                #chitaem pervuyu stroku v peremennuyu
print("str in file: " + str(line))                  #pokazivaem, chto prochitali
fo.close()                                          #zakrivaem file
dlinline = len(line)
markspace = ' '
marktab = '\t'
zaglushka = ''
print('-------- str replaced ---------------')
for i in range(len(line)):
    zaglushka = zaglushka + line[i]
    if line[i] == marktab:
        zaglushka = zaglushka.replace(marktab, markspace*4)
       # zaglushka = zaglushka + markspace *4

#print(zaglushka)
line = zaglushka
print(line)