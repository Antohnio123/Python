s_n = input("Введите пятизначное число :")
s_nl=list(s_n)
print ("  Число: ",s_n)
for i in range(0,len(s_nl)) :
    print(" {} цифра равна {} ".format(str(i+1),s_nl[i]))
