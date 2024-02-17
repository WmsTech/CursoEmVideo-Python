cores = {'fim': '\033[m','branco': '\033[30m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'lilas': '\033[35m', 'magenta': '\033[36m', 'cinza': '\033[37m'}


def leiaInt(dado):
    while True:
        n = str(input(dado))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print(f'{cores["vermelho"]}[>> ERRO <<] Dado Invalido. Digite um valor Inteiro!{cores["fim"]}')
    return n


num = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {num}')


