attlst=[[True, False, True, True, False],
        [False, False, True, True, False],
        [True, True, False, True, False],
        [False, True, True, True, True],
        [False, True, False, False, True]]

def get_bs(attlst):
    s=[sum(ls) for ls in list(zip(*attlst))]
    return s.index(max(s))


print(get_bs(attlst))
