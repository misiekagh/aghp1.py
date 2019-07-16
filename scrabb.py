scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def word_score(word):
    score=0
    for l in word:
        score+=scores[l]
    return score

def word_score2(word):
    return sum([scores[l] for l in word])

print(word_score('tomcat'))
print(word_score2('tomcat'))

fd={'a':10,'b':20,'c':3}
sd={'b':3, 'd':2, 'a':1}

def merg_with_add(d1, d2):
    md={}
    for k in d1.keys() | d2.keys():
        md[k] = 0
        if k in d1: md[k]+=d1[k]
        if k in d2: md[k]+=d2[k]
    return md


print(merg_with_add(fd,sd))
