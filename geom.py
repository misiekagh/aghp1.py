PI=3.1415

def ob_circ(radius=0):
    return PI*(radius**2)


def ob_triangle(base=0,heigth=0):
    return (base*heigth)/2


def ob_square(a,b=0):
    if b:
        return a*b
    else:
        return a*a

if __name__=="__main__":
    print(f'Pole kola: {ob_circ(3)}')
    print(f'Pole trojkata: {ob_triangle(2,2)}')
    print(f'Pole kwadratu: {ob_square(2)}')

    ans=''
    while(ans != 'x'):
        ans=input('Sel fig (s)quare (c)ircle (t)riangle or e(x)it: ')
        if ans=='s':
            print(ob_square(float(input('Enter side: '))))
        elif ans=='c':
            print(f'Pole kola:'.format(ob_circ(float(input('Enter radius: ')))))
        elif ans=='t':
            o=ob_triangle(float(input('Enter bas: ')))
            print(f'Pole trojkata: {o}')
