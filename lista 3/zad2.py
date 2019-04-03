from numpy import *
from cs50 import get_float
from math import pi


# definicje
def menu():
    print('\n',
          '_'*60, '\n'
          'Lista dostępnych figur:', '\n'
          '[1] - koło \n'
          '[2] - romb \n'
          '[3] - prostokąt \n'
          '[4] - trójkąt \n')


# inputy
x = get_float('podaj #1 długość: ')
while x <= 0:
    print('### wprowadz wartość większą od 0.')
    x = get_float('podaj #1 długość: ')
y = get_float('podaj #2 długość: ')
while y <= 0:
    print('### wprowadz wartość większą od 0.')
    y = get_float('podaj #2 długość: ')


# figura 1
while True:
    menu()
    k = input("wybierz #1 figurę: \n >> ")
    if k == '1':
        p1 = round(pi * x ** 2, 2)
        l1 = 'kola'
        break
    elif k == '2':
        p1 = (x * y) / 2
        l1 = 'rombu'
        break
    elif k == '3':
        p1 = x*y
        l1 = 'prostokatu'
        break
    elif k == '4':
        p1 = (x * y) / 2
        l1 = 'trójkąta'
        break
    else:
        print('nie ma takiej figury')


# figura 2
while True:
    menu()
    k2 = input("wybierz #2 figurę: \n >> ")
    if k2 == '1':
        p2 = round(pi * x ** 2, 2)
        l2 = 'kola'
        break
    elif k2 == '2':
        p2 = (x * y) / 2
        l2 = 'rombu'
        break
    elif k2 == '3':
        p2 = x*y
        l2 = 'prostokata'
        break
    elif k2 == '4':
        p2 = (x * y) / 2
        l2 = 'trójkąta'
        break
    else:
        print('nie ma takiej figury')


print('\n\n')
print('#'*40)
print('\n')


# porównanie pola
if p1 == p2:
    print('_'*60)
    print('pola figur są sobie równe')
    print('_'*60)
elif p1 > p2:
    print('_' * 60)
    print('pole', l1, 'jest większe od pola', l2)
    print('pole', l1, '=', p1)
    print('pole', l2, '=', p2)
    print('ich różnica wynosi: ', p1 - p2)
    print('_' * 60)
elif p1 < p2:
    print('_' * 60)
    print('pole', l2, ' jest większe od pola', l1)
    print('pole', l1, '=', p1)
    print('pole', l2, '=', p2)
    print('ich różnica wynosi: ', p2 - p1)
    print('_' * 60)
