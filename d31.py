states = ['California', 'Texas', 'New York', 'Florida', 'Illinois']
capitals = ['Sacramento', 'Austin', 'Albany', 'Tallahassee', 'Springfield']

usa={s:c for s,c in zip(states,capitals)}

print(usa)

from decimal import Decimal

a=Decimal('0.2')
b=Decimal('0.3')
print(repr(a))
