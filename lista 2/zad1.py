from cs50 import get_int
from math import pi

x = get_int('podaj promień #1 koła: ')
y = get_int('podaj promień #2 koła: ')


def kolo(r):
    print('_' * 20)
    print('koło o promieniu', r, '\n')
    print('pole =', round(pi * r ** 2, 2))
    print('obwód =', round(2 * pi * r, 2))


kolo(x)

kolo(y)
