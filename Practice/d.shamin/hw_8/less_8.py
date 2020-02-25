############################ Задача 1
def len_custom(lst):
    i = 0
    for j in lst:
        i += 1
    print(i)

lst_n = [2,4,6,8,10]
len_custom(lst_n)

print()
############################ Задача 2
def rev_custom(lst):
    i = 0
    new_l = []
    for j in lst:
        i += 1
    n = i - 1
    for j in lst:
        new_l.append(lst[n])
        n -= 1
    print(new_l)

rev_custom(lst_n)

print()
############################ Задача 3



print()
############################ Задача 4

def to_title(name):
    spl = name.split()
    new_srt = ""
    for i in spl:
        new_srt = new_srt + i.capitalize() + " "
    print(new_srt.rstrip())

srt = 'orlov      Ilya          evgenyevich'
to_title(srt)

print()
############################ Задача 5

def count_symbol(srt, i):
    print(srt.count(i))

srt_l = "Hi, Elvis, I am here!"
count_symbol(srt_l, "e")

print()
############################ Задача 6

