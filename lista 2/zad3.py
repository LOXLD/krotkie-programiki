from cs50 import get_int

x = get_int('x:')
y = get_int('y:')

podzielnosc = '\n X jest podzielne przez Y' if x % y == 0 else '\n X nie jest podzielne przez Y '

print(podzielnosc)
