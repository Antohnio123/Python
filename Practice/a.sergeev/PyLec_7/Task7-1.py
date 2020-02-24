import datetime

first_date=input("Vvedite year, month, day: ")
second_date=input("Vvedite year, month, day: ")
first_date=first_date.split(" ")
second_date=second_date.split(" ")

first_date_list=datetime.date(int(first_date[0]), int(first_date[1]), int(first_date[2]))
second_date_list=datetime.date(int(second_date[0]), int(second_date[1]), int(second_date[2]))
day1=str(second_date_list-first_date_list)
day1=int(day1.split()[0])
rabochih_day=float(round((day1*(5/7))))

print("Rabochih dney ", rabochih_day)
