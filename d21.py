text='If the implementation is hard to explain, it\'s a bad idea. \
        If the implementation is easy to explain, it may be a good idea.'

def rev_word(word):
#    return ''.join(list(reversed(word)))
    return ''.join(reversed(word))

def rev_sent(sentence):
    return reversed([rev_word(w) for w in sentence.split()])

def join_list(lst):
    return ' '.join(lst)


r=join_list(rev_sent(text))
print(r)

print(join_list(rev_sent(r)))
