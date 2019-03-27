from cs50 import get_int

print('-' * 35)
x = get_int('wprowadz X: ')
y = get_int('wprowadz Y: ')
print('-' * 35)


def dziel():
    if x % y == 0:
        print('X / Y = ', int(x / y), )
    elif x < y:
        print('X jest mniejsze od Y (ale X/Y=', round(x / y, 2), ')')
    else:
        print('X / Y = ', x // y, 'całych i', x % y, 'reszty')


def pary(a, b):
    if a != 0 and b != 0:
        if a % 2 == 0 and b % 2 == 0:
            print('Obie liczby są parzyste  :)')
            print('-' * 35)
            dziel()
        else:
            print('Obie liczby muszą być parzyste.')
    else:
        print('Pamietaj cholero NIE dziel przez zero')


pary(x, y)
