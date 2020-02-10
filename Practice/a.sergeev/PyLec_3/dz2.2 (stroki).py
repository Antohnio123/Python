S="hphqhwhehrhthyhuhihohohoh"
Sf = S.find('h')
Sl = S.rfind('h')
Sf1 = S[:Sf + 1]
Sl1 = S[Sl:]
Sp = S[Sf + 1 : Sl]
print (str(Sf1) + str(Sp.replace('h','H')) + str(Sl1))

