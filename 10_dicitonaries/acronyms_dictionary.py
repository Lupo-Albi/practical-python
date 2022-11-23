acronyms = {
    'LOL': 'laugh out loud'
}
print(acronyms)

acronyms['IDK'] = "I don't know"
acronyms['TBH'] = 'to be honest'
print(acronyms)


acronyms['TBH'] = 'honestly'
print(acronyms['TBH'])

del acronyms['TBH']
print(acronyms)
acronyms['TBH'] = 'to be honest'

# Accessing a key that doesn't exist without causing an error
# definition = acronyms['BTW'] # KeyError
definition = acronyms.get('BTW')
print(definition)  # None

if definition:
    print(definition)
else:
    print("Key doesn't exist")

sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)
