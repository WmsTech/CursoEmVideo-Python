from random import randint
from time import sleep
numeros = []


def sorteia(num):
    print('Irei sortear 5 numeros e guardá-los. Sorteando -> ', end='')
    for c in range(0, 5):
        num.append(randint(0, 10))
        sleep(0.5)
        print(f'{num[c]}  ', end='')
    print(f'FIM!')


def somaPar(num):
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(f'Com os numeros {num} a soma dos numeros pares é {soma}.')


sorteia(numeros)
somaPar(numeros)
