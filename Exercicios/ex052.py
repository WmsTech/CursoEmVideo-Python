from time import sleep
cores = {'fim': '\033[m','branco': '\033[30m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'lilas': '\033[35m', 'magenta': '\033[36m', 'cinza': '\033[37m', 'preto': '\033[7:40m'}

print('{}'.format('<>') * 45)
print('{:^90}'.format('Numeros Primos'))
print('{}'.format('<>') * 45)
print('{}{}{}'.format(cores['amarelo'], 'Um numero primo é um numero divisivel por 1 e por ele mesmo.', cores['fim']))

n = int(input('Digite um numero que vou informa se é um numero primo. \n-> '))
div = 0
print('{} é divisel por:'.format(n))
for c in range(1, n + 1):
    sleep(1)
    if n % c == 0:
        div += 1
        print('{}{}{} '.format(cores['verde'], c, cores['fim']), end=' ')
    else:
        print('{}{}{} '.format(cores['vermelho'], c, cores['fim']), end=' ')

if div == 2:
    print('\nComo {} e divisivel apenas por 1 e por ele mesmo, logo {} é um numero primo!'.format(n, n))
else:
    print('\nO numero {} não é um numero primo!'.format(n))