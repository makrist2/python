word = 'downstream'
word = word.lower()
if len(word) == len(set(word)):
    print('Isogram')
else:
    print('Not an isogram')


