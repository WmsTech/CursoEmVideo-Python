def fatorial(numero, mostra=False):
    """
    -> Calcula o fatorial de um numero
    :param numero: numero a ser calculado
    :param mostra: parametro opcional para mostrar ou não o calculo
    :return: retorna o fatorial de numero
    """
    f = 1
    if mostra:
        print(f'\n  {numero}! = ', end='')
        for c in range(numero, 0, -1):
            f *= c
            if c == 1: 
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
    else:
        for c in range(numero, 0, -1):
            f *= c
    return f


print('>'*5, 'Fatorial', '<'*5)
numero = int(input('Digite o numero: '))
decisão = int(input('Digite qualquer numero para mostrar o calculo (0 para não mostrar): '))
mostra = False if decisão == 0 else True
print(f'O fatorial de {numero} é: ', end='')
print(f'{fatorial(numero, mostra)}')
input()
help(fatorial)

