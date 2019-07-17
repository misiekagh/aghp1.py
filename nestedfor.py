from pprint import pprint
lst=[]
for i in range(5):
    lst.append([i],)
    for j in range(4):
        lst[i].append(j)
pprint(lst)
