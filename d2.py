def exp_bonuz(nam, exp, sal):
    if exp<=1: return sal*0.05
    elif exp<=5: return sal*0.1
    else: return sal*0.15

def sal_bonuz(nam, exp, sal):
    if sal<2000: return sal*0.12
    elif 2000<=sal<10000: return sal*0.08
    else: return 0.0

def nam_bonuz(nam, exp, sal):
    if len(nam)<3: return sal*0.05
    elif len(nam)<5: return sal*0.1
    else: return sal*0.15

bonuz_lst=[exp_bonuz, sal_bonuz, nam_bonuz]

def calc_best_bonus(name, sal, exp):
    return max([bonus(name, exp, sal) for bonus in bonuz_lst])

def calc_new_sal(name,sal,exp):
    return name, sal+sal*calc_best_bonus(name,exp,sal)

prac_lst=[['Jan Kowalski', 24, 4500],
          ['Janusz Biznesu', 10, 3200],
          ['Mata Hari', 1, 2500]]

for prac in prac_lst:
    print(calc_new_sal(*prac))

print([1,2,3,4][::-2])