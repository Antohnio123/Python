s = str(input('Input string (at least, five characters!): '))
l = len(s)
if l<5:
    print('Your string is too short!')
else:
    print('The third character: ' + s[2],
          'The second to last character: ' + s[-2],
          'Five first characters: ' + s[0:5],
          'Without two last characters: ' + s[0:(l - 2)],
          'Characters with even index: ' + s[0::2],
          'Characters with odd index: ' + s[1::2],
          'Reverse order: ' + s[::-1],
          'From the last character thru one: ' + s[-1::-2],
          "String's length: " + str(l), sep = '\n')