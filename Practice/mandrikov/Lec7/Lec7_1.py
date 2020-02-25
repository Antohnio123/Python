import datetime

fromdate = datetime.date(2020, 2, 20)
todate = datetime.date(2020, 3, 6)
daygenerator = (fromdate + datetime.timedelta(x) for x in range((todate - fromdate).days + 1))
res = sum(1 for day in daygenerator if day.isoweekday() < 7)
print(res//7*5)
