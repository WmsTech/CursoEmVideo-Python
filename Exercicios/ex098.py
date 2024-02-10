from time import sleep


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: salto ou passo da contagem
    :return: sem retorno
    """
    aux = 0 # Uma variavel utilizada apenas para apresentar no print, para preservar o valor das variaveis principais
    ff = 0 # Uma variavel para determinar o limite da contagem no for, para preservar o valor das variaveis principais
    if p == 0:
        p = 1
    if i > f:
        if p > 0:
            aux = p
            p = p *(-1)
        else:
            aux = p *(-1)
        ff = f - 1
    else:
        aux = p
        if p < 0:
            aux = p = p *(-1)
        ff = f + 1
    print(f'A contagem de {i} até {f} de {aux} em {aux} é: ')
    for c in range(i, ff, p):
        sleep(0.5)
        print(f'{c} ', end='')
    print()


def linha():
    print('-' * 50)


print(f'>' * 5, f'Contador', '<' * 5)
linha()
contador(1, 10, 1)
linha()
contador(10, 0, -2)
linha()
print(f'Digite os dados para a contagem.')
inicio = int(input('Inicio da contagem: '))
fim = int(input('Final da contagem: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
input()
help(contador)

