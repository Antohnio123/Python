def clockwork(a):
    if a>720:
        print('Sorry, it is more than one day')
    else:
        print('It is ' + str(a // 30) + ' hours and ' + str((a % 30) * 2) + ' minutes')
degrees = int(input("How many degrees did the hour hand turn since the beginning of the day? "))
clockwork(degrees)