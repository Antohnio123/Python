def converter(a):
    if a>86400:
        print('Sorry, it is more than one day')
    else:
        print('It is ' + str(a // 3600) + ' hours and ' + str((a % 3600) // 60) + ' minutes')
time = int(input("Input time in seconds: "))
converter(time)