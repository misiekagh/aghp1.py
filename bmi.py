def licz_bmi(waga,wzrost):
    bmi = waga/wzrost **2
    if bmi < 18.5:
        result='niedowaga'
    elif bmi > 25:
        result = 'nadwga'
    else:
        result = 'poprawna'

    return result,bmi

if __name__=='__main__':
    waga=float(input('Podaj wage'))
    wzrost=float(input('Podaj wzrost'))
    print('Wynik: {}'.format(licz_bmi(waga, wzrost)))
    print(f'Wynik{licz_bmi(72,1.86)}')1
