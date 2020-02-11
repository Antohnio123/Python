## Числа
# Первое задание
print("Enter the amount of seconds passed:")
k = int(input())
h = k//60//60
m = round((k-3600*h)//60)
print(f"It is {h} hours {m} minutes.")

# Второе задание
print("Enter the angle of the clock:")
d = int(input())
h = round(d//30)
m = round((d-30*h)*2)
print(f"It is {h} hours {m} minutes")

## Строки
# Первое задание
s1 = str(input("Enter the string (at least 5 characters):"))
print(s1)
print(s1[2])
print(s1[-2])
print(s1[0:5])
print(s1[0:-2])
print(s1[::2])
print(s1[1::2])
print(s1[::-1])
print(s1[-1::-2])
print(len(s1))

# Второе задание
s2 = str(input("Enter the string:"))
print(s2)
cnt = s2.count('h')
fnd = s2.find('h')
s2 = s2.replace('h', 'H', cnt - 1)
s2 = s2[:fnd] + 'h' + s2[fnd + 1:]
print(s2)

# Третье задание
s3 = input("Enter two words: ")
s31=s3.split(sep=" ", maxsplit = 2)
print(s31[1]+" "+s31[0])
