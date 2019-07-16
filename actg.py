from random import randint

genes=['A', 'C', 'T', 'G']
def get_genes(glen):
    return [y for x in range(glen) for y in genes[randint(0,3)]]

def count_humm(hlst):
    sum=0
    if len(hlst)==1:
        return int(hlst[0][0]!=hlst[0][1])
    else:
        return int(hlst[0][0]!=hlst[0][1])+count_humm(hlst[1:])

GEN_COUNT=20
child=get_genes(GEN_COUNT)
man1=get_genes(GEN_COUNT)
man2=get_genes(GEN_COUNT)

pair1=list(zip(child,man1))
pair2=list(zip(child,man2))
print('man1', pair1)
print('man2', pair2)

print(f'Odleg1 man1: {count_humm(pair1)}')
print(f'Odleg2 man2: {count_humm(pair2)}')