from decimal import Decimal as dec

class Wal(dec):
    def __init__(self, w):
        super().__init__()

class Kantor:
    def __init__(self):
        wd={'EUR': '4.2729', 'GBP': '4.7508', 'USD': '3.8066', 'NOK': '0.4401', 'SEK': '0.4020', 'CHF': '3.8410'}
        self.waluty={ w:Wal(k) for w,k in wd.items()}

    def wymien(self, waluta,suma):
        try:
            return dec(self.waluty[waluta]*dec(suma))
        except Exception as e:
            return e, 'Brak waluty?'

if __name__=='__main__':
    a = Kantor()
    print(a.wymien('EUR','150'))
