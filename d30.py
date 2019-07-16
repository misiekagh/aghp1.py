def capit(word):
    return word[0].upper()+word[1:]

def capit_sent(sen):
    return [capit(w) for w in sen.split()]

def crea_dict(sent):
    return {w:c for w, c in zip(sent.split(),capit_sent(sent))}

print(capit_sent('aaa bbb ccc'))
print(crea_dict('uuuu wwww rrrr'))