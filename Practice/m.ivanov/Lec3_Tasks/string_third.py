s = input('Enter two words with a space between them: ') .split()
s.reverse()
s = ' '.join(s)
print('So the last shall be first: ' + s)