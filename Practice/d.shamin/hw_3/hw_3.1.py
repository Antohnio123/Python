from tkinter import *
# import math
from tkinter import messagebox as mb

# 1.сколько целых часов h и целых минут m прошло с начала суток


def time():
    k = ent_time.get()
    if k.isdigit():
        k = int(k)
        if k > 86399:
            mb.showerror("Ошибка", "Это больше чем 24 часа!")
        else:
            hrs = k // 3600
            res_min_left = k % 3600
            mnts = res_min_left // 60
            #mb.showinfo("Текущее время", curr_time)
            lbl_time_res.configure(text=c_time(hrs,mnts))
    else:
        mb.showerror("Текущее время", "Это должно быть целым числом.")


# 2.сколько целых часов h и целых минут m прошло с начала суток
def clock():
    try:
        h = float(ent_clock.get())
        if h > 359:
            mb.showerror("Error", "360 maximum!")
        else:
            x = 0
            y = 30
            i = 0
            j = 0.5
            hrs = 0
            mnts = 0
            for hrs in range(0, 12):
                if x < h <= y:
                    break
                else:
                    x += 30
                    y += 30

            grad = h - x

            for mnts in range(0, 60):
                if i <= grad < j:
                    break
                else:
                    i += 0.5
                    j += 0.5
            if hrs == 0:
                hrs = 12
            #mb.showinfo("Стрелка часов", curr_time)
            lbl_clock_res.configure(text=c_time(hrs,mnts))
    except ValueError:
        mb.showerror("Error", "Wrong characters!")


def c_time(hh, mm):
    curr_time = "Сейчас " + str(hh) + " часов " + str(mm) + " минут."
    return curr_time


hrs = "__"

mnts = "__"


wnd = Tk()
wnd.title("Счётчик")
wnd.geometry("600x100")
lbl_time = Label(wnd, text="Секунды", font=("Consolas", 12, "bold"), padx=10, pady=10)
lbl_time.grid(column=0, row=0)
ent_time = Entry(wnd, width=10)
ent_time.grid(column=1, row=0, padx=10)
btn_time = Button(wnd, text="Показать", command=time)
btn_time.grid(column=2, row=0)
lbl_time_res = Label(wnd, text=c_time(hrs,mnts), font=("Consolas", 12, "bold"), padx=10, pady=10)
lbl_time_res.grid(column=3, row=0)


lbl_clock = Label(wnd, text="Градус стрелки", font=("Consolas", 12, "bold"), padx=10, pady=10)
lbl_clock.grid(column=0, row=1)
ent_clock = Entry(wnd, width=10)
ent_clock.grid(column=1, row=1, padx=10)
btn_clock = Button(wnd, text="Показать", command=clock)
btn_clock.grid(column=2, row=1)
lbl_clock_res = Label(wnd, text=c_time(hrs,mnts), font=("Consolas", 12, "bold"), padx=10, pady=10)
lbl_clock_res.grid(column=3, row=1)
wnd.mainloop()
