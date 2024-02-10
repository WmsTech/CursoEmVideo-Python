cores = {'fim': '\033[m','branco': '\033[30m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'lilas': '\033[35m', 'magenta': '\033[36m', 'cinza': '\033[37m'}

print('{}{:^40}{}'.format(cores['azul'] ,'Comparador de Numeros', cores['fim']))
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print('Na comparação entre {}{}{} e {}{}{}, o {}{}{} numero é Maior!'.format(cores['azul'], n1, cores['fim'], cores['amarelo'], n2, cores['fim'], cores['verde'], 'PRIMEIRO', cores['fim']))
elif n1 < n2:
    print('Na comparação entre {}{}{} e {}{}{}, o {}{}{} numero é Maior!'.format(cores['azul'], n1, cores['fim'], cores['amarelo'], n2, cores['fim'], cores['verde'], 'SEGUNDO', cores['fim']))
else:
    print(print('Na comparação entre {}{}{} e {}{}{}, os numeros são iguais!'.format(cores['azul'], n1, cores['fim'], cores['amarelo'], n2, cores['fim'])))