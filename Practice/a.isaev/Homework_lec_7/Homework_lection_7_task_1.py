
import datetime

def dif_time():
    time_1 = input("Input first date Ymd without spaces: ")
    time_dt_1 = datetime.datetime.strptime(time_1, '%Y%m%d')
    time_2 = input("Input second date Ymd without spaces: ")
    time_dt_2 = datetime.datetime.strptime(time_2, '%Y%m%d')
    delta = time_dt_2 - time_dt_1
    days = delta.days
    weeks = round(days / 7)
    weeks_module = days % 7

    if weeks_module == 0:
        work_days = days - (weeks * 2)
        print(work_days)
    else:
        if weeks_module ==6:
            work_days = days - (weeks * 2) - 1
            print(work_days)
        else:
            work_days = days - (weeks * 2)
            print(work_days)

dif_time()



