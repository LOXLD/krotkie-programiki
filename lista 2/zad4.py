from cs50 import get_int

x = get_int('x:')
y = get_int('y:')

podzielnosc = x / y
podzielnosc = format(podzielnosc, '.2f')

print('\n')
print(podzielnosc)
