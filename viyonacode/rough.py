names = {}
names['a'] = ['anmol', 'aarav']
names['b'] = ['ba', 'berndi', 'benny']
names['d'] = ['delfina', 'david', 'dominika']


character = input('give a letter:')

# TODO: find name
try:
    wert = 0
    name = names[character][0]
    for wort in names[character]:
        if wort < name:
            name = wort
except KeyError:
    name = ''
raise TypeError('')

 #   wert = len(wort)
  #  if wert>name:
   #     name = wert



print('longest name starting with character is ', name)