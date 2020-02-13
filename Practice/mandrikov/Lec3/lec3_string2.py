s = input("Write a string")
s1 = s[s.find('h'):s.rfind('h')]
s1 = s1.replace('h', 'H')
print(s[:s.find('h') + 1] + s1 + s[s.rfind('h'):])
