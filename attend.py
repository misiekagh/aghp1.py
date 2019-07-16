def parse_str(attstr):
    attlst=[]
    for id in attstr:
        attlst.append(id=='T')
    return attlst

def cnt_pres(attlst):
    """
    Liczy obecnosc
    :param attlst: lista
    :return: liczba osob
    """
    return sum(attlst), sum(attlst)/len(attlst)


