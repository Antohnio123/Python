s = str(input('Input string: '))
i = s.count('h')
if i<3:
    print('Your string has not changed:' + s)
else:
    j = s.find ('h')
    s = s.replace('h','H',i - 1)
    s = s[:j] + 'h' + s[j + 1:]
    print('Your string has changed: ' + s)
