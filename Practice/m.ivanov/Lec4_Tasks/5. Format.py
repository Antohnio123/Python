mydict = {"comma":",","apostrophe": "'", "dot": ".", "space": " "}
s = 'Sorry{comma}{space}I{space}didn{apostrophe}t{space}understand{space}this{space}task{dot}'.format(**mydict)
print(s)
