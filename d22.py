word=' '
while (len(word)):
    word=input('Gimme word! ENTER to exit.: ').lower()
    if len(word) == len(set(word)):
        print('Isogram')
    else:
        print('Not isogram')
