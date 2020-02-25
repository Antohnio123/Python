from datetime import datetime, date, time
dd1=date(2005, 7, 15)
dd2 = d2 = date(2005, 9, 3)
def NumberWorkDays(d1 = date(2005, 7, 15), d2 = date(2005, 7, 3)) :
    delta = d2 - d1
    if delta.days < 0 :
        dn1, dn2 = d2, d1
    else :
        dn1, dn2 = d1, d2
    delta = dn2 - dn1
    full_weeks = (delta.days) // 7
    remainder = (delta.days) % 7
    w1 = datetime.isoweekday(dn1)
    w2 = datetime.isoweekday(dn2)
    if w2 < w1 :
        w2 = w2 + 7
    i = 0
    j = 0
    while i < 14 :
        i += 1
        if (i > w1) and (i !=6) and (i!=7) and (i < w2) :
            j += 1
    work_days = full_weeks * 5 + j
    return work_days

print("Количество рабочих дней между {}  и {} равно :".format(dd1,dd2), NumberWorkDays(dd1, dd2))
