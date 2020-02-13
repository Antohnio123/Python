dano = 50  # sekund

if dano // 3600 > 0:
    chasov = dano // 3600
    minut = (dano - (chasov * 3600)) // 60
    sekund = dano - ((chasov * 3600) + (minut * 60))
    print('chasov = ' + str(chasov))
    print('minut = ' + str(minut))
    print('sekund =  ' + str(sekund))

elif dano < 3600 and dano > 59:
    minutmh = dano // 60
    sekundmh = dano - (minutmh * 60)
    print('chasov = 0')
    print('minut = ' + str(minutmh))
    print('sekund = ' + str(sekundmh))

else:
    print('chasov = 0')
    print('minut = 0')
    print('sekund = ' + str(dano))

#---------------------------------------------------------
dano = 60                #sekund

ah = 0
mh = 0

if dano // 3600 > 0:
    chasov = dano // 3600
    minut = (dano - (chasov * 3600)) // 60
    sekund =  dano - ((chasov * 3600) + (minut * 60))
    ah = chasov
    mh = minut

elif dano < 3600 and dano > 59:
    minutmh = dano // 60
    sekundmh = dano - (minutmh * 60)
    ah = 0
    mh = minutmh

else:
    ah=0
    mh=0

print('It is ' + str(ah) + ' hours ' + str(mh) + ' minutes.')

#-----------------------------------------------------------

dano = 60.51                #gradus chasovoy strelki

odinchas = 360/12                   # = 30 grad
odnaminuta = (360/12) / 60          # = 0.5 grad
odnasekunda = ((360/12) / 60) / 60  # = 0.083333333333

proshlochasov = dano // odinchas
proshlominut = (dano - proshlochasov) * odnaminuta
sekundproshlovoobshe = (dano/odnasekunda)


if sekundproshlovoobshe // 3600 > 0:
    chasov = sekundproshlovoobshe // 3600
    minut = (sekundproshlovoobshe - (chasov * 3600)) // 60
    sekund = sekundproshlovoobshe - ((chasov * 3600) + (minut * 60))
    print('chasov = ' + str(chasov))
    print('minut = ' + str(minut))
    print('sekund =  ' + str(sekund))

elif sekundproshlovoobshe < 3600 and dano > 59:
    minutmh = sekundproshlovoobshe // 60
    sekundmh = sekundproshlovoobshe - (minutmh * 60)
    print('chasov = 0')
    print('minut = ' + str(minutmh))
    print('sekund = ' + str(sekundmh))

else:
    print('chasov = 0')
    print('minut = 0')
    print('sekund = ' + str(sekundproshlovoobshe))

print('It is ' + str(chasov) + ' hours ' + str(minut) + ' minutes.')

#----------------------------------------------------------------


# vivesti 3y simvol v str
s = 'string_1 print 3 sybol'
print("zadanie-1, stroki")
print(s[2])

# -------------------------------------------------------
# vivesti predposledniy simvol stroki
s2 = 'string_2 print pre last symbl'
s2len = len(s2)
# pochemy avtozamena prosit pisat "s2len: int = len(s2)"  ???
print(" ")
print("zadanie-2, stroki")
print(s2[s2len - 2])
# pochemu -1 posledniy, a -2 predposl  ???

# variant2 zadanie-2 stroki
counts2 = 0
for x in s2:
    counts2 += 1
print(" ")
print("zadanie-2, stroki - variant 2")
print(s2[counts2 - 2])

# --------------------------------------------------------
# vivesti 5 pervih simvolov stroki
s3 = 'string_3 print 5 first symbls'
s3len = len(s3)
print(" ")
print("zadanie-3, stroki")
print(s3[: 5])

# variant2 zadanie-3 stroki
counts3 = 0
s3_ogranichenie = 5
for xx in s3:
    if counts3 == s3_ogranichenie:
        break
    counts3 += 1
print(" ")
print("zadanie-3, stroki - variant 2")
print(s3[:counts3])

# --------------------------------------------------------
# vivesti vsu stroku krome posledn 2 simvolov
s4 = 'string_4 print all string besides 2 last symbols'
s4len = len(s4)
print(" ")
print("zadanie-4, stroki")
print(s4[: s4len - 2])

# variant2 zadanie-4 stroki
counts4 = 0
s4_obrez = 2
for xxx in s4:
    counts4 += 1
print(" ")
print("zadanie-4, stroki - variant 2")
print(s4[:counts4 - s4_obrez])

# --------------------------------------------------------
# vivesti vse chetnie simvoly, nachinaya ot 0 - t.e. 1,3,5...
s5 = 'string_5 print all even symbols 123456789'
s5len = len(s5)
print(' ')
print("zadanie-5, stroki")
print(s5[0:s5len:2])

# variant2 zadanie-5 stroki
news5 = ''
# for xxxx in s5:
#    if xxxx % 2 == 0:
#        news5 = news5 + s5[xxxx]
# pochemu nelzya reshit ciklom FOR   ???
i = 0
while i != s5len:
    i += 1
    if i % 2 == 0:
        news5 = news5 + s5[i]
        continue
# kuda delsya perviy simvol   ????
print(' ')
print("zadanie-5, stroki - variant 2")
print(news5)
print('zadan-5 var 2 - not correct')

# --------------------------------------------------------
# vivesti vse ne chetnie simvoly, nachinaya ot 0 - t.e. 0,2,4...
# beru kazhdiy 2 simvol
s6 = 'string_5 print all odd symbols 0123456789'
s6len = len(s6)
news6 = ''
print(' ')
print("zadanie-6, stroki")
print(s6[1:s5len:2])
# variant2 zadanie-6 stroki
# for xxxx in s6:
#    if xxxx % 2 == 1
#    news5 = 1
# news6 = news6 + s6[xxxx]

# ii = 0
# while ii != s6len:
#    i += 1
#    if ii % 2 == 1:
#        news6 = news6 + s6[ii]
#        continue
#
print(' ')
print('zadanie-6, stroki - variant 2')
print(news6)

# --------------------------------------------------------
# vivesti vse simvoli v obratnom poryadke
# inversiya stroki
s7 = 'string_7 reverse 123456789'
s7len = len(s7)
print(' ')
print("zadanie-7, stroki")
print(s7[::-1])

# --------------------------------------------------------
# vivesti vse simvoli cherez odin v obratnom poryadke
s8 = 'string_8 123456789 cherez odin'
s8len = len(s8)
revs8 = s8[::-1]
vivods8 = ''
i8 = 0
for i8 in range(1, s8len, 2):
    vivods8 = vivods8 + s8[i8]
print(' ')
print("zadanie-8, stroki")
print(vivods8)
print("ouptut is not correct")


# --------------------------------------------------------
# vivesti dlinu stroki
s9 = 'string_9 123456789'
s9len = len(s9)
print(' ')
print("zadanie-9, stroki")
print("dlina stroki = " + str(s9len))

# --------------------------------------------------------
# zamenit vsr h na H krome 1 pervogo i poslednego
s10 ="hhhaaDDHHHrrrhhhttthhEEzzhh"
s1 = len(s)
s2 = len(s) - 2
sr = 'h'

if s[0] == 'h':
    rangstart = 1
else:
    rangstart = 0

if s[s2] == 'h':
    rangstop = s2
else:
    rangstopt = s1

# for i in range(0, s2):
#    s=s.replace('h', 'H')
# if s[0] == 'H':
# s[0] = 'h'

# print(s)

# print(s[s2])


#------------------------------
# zamena 2h elemenov mestami bez cikla i if
s = "one two"

a = s.split( )

prom1 = str(a[0])
prom2 = str(a[1])
prom3 = ' '
vihod = prom2 + prom3 + prom1

print(vihod)