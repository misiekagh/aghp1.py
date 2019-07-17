kwiatki = {}

with open('iris.data') as plik:
    for l in plik:
        *vals,name=l.rstrip('\n').split(',')

        if name not in kwiatki.keys():
            kwiatki[name]=[[], [], [], []]

        a,b,c,d = vals
        kwiatki[name][0].append(float(a))
        kwiatki[name][1].append(float(b))
        kwiatki[name][2].append(float(c))
        kwiatki[name][3].append(float(d))

with open('kwiatki.txt','w') as file:
    for k,v in kwiatki.items():
        file.write(f'Kwiatek {k} średnie {[sum(k)/len(k) for k in v]}\n')
