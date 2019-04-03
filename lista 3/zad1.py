from numpy import *
from cs50 import get_float
from math import pi

print('+-'*20)
print('Witaj w programie liczącym śmieszne rzeczy.')


def menu():
    print('\n',
          '-'*80, '\n'
          'Wybierz figurę, której pole chciałbyś obliczyć:', '\n'
          '[1] - koło \n'
          '[2] - romb \n'
          '[3] - prostokąt \n'
          '[4] - trójkąt \n'
          '[x] - aby zakończyć program \n')


def kolo(r):
    print('_' * 30)
    print('koło o promieniu', r, '\n')
    print('pole =', round(pi * r ** 2, 2))
    print('_' * 30)


def romb(e, f):
    print('_' * 30)
    print('rąb o przekątnych', e, 'i', f, '\n')
    print('pole =', (e * f) / 2)
    print('_' * 30)


def prostokat(a, b):
    print('_' * 30)
    print('prostokąt o bokach', a, 'i', b, '\n')
    print('pole =', a*b)
    print('_' * 30)


def trojkat(d, h):
    print('_' * 30)
    print('trójkąt o podstawie', d, 'i wysokości', h, '\n')
    print('pole =', (d*h)/2)
    print('_' * 30)


while True:
    menu()
    k = input("wybierz operację: \n >> ")
    print('\n')
    if k == 'x':
        print('>> Dzięki za skorzystanie z programu <<')
        break
    elif k == '1':
        r = get_float('podaj promień koła: ')
        while r < 0:
            print('wprowadz dodatnia wartość.', '\n')
            r = get_float('podaj promień koła: ')

        kolo(r)
    elif k == '2':
        e = get_float('podaj długość #1 przekatnej: ')
        while e < 0:
            print('### wprowadz dodatnia wartość.')
            e = get_float('podaj długość #1 przekatnej: ')
        f = get_float('podaj długość #2 przekatnej: ')
        while f < 0:
            print('### wprowadz dodatnia wartość.')
            f = get_float('podaj długość #2 przekatnej: ')
        romb(e, f)
    elif k == '3':
        a = get_float('podaj długość #1 boku: ')
        while a < 0:
            print('### wprowadz dodatnia wartość.')
            a = get_float('podaj długość #1 boku:')
        b = get_float('podaj długość #2 boku: ')
        while b < 0:
            print('### wprowadz dodatnia wartość.')
            b = get_float('podaj długość #2 boku:')
        prostokat(a, b)
    elif k == '4':
        d = get_float('podaj długość podstawy trójkąta: ')
        while d < 0:
            print('### wprowadz dodatnia wartość.')
            d = get_float('podaj długość podstawy trójkąta: ')
        h = get_float('podaj wysokość trójkąta: ')
        while h < 0:
            print('### wprowadz dodatnia wartość.')
            h = get_float('podaj wysokość trójkąta: ')
        trojkat(d, h)
    else:
        print('Nie ma takiej funkcji,\n'
              'spróbuj ponownie')
