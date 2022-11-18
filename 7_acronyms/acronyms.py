acronyms = ['LOL', 'IDK', 'BFF']
print(acronyms)

acronyms.append('SMH')
acronyms.append('NGL')
acronyms.append('TBH')
print(acronyms)

del acronyms[2]
acronyms.remove('TBH')
print(acronyms)

acronyms.append('LMK')
word = 'LMK'

if word in acronyms:
    print(word + ' is in the list')
else:
    print(word + ' is NOT in the list')

for acronym in acronyms:
    print(acronym)
