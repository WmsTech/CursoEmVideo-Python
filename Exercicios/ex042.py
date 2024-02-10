cores = {'fim': '\033[m','branco': '\033[30m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'lilas': '\033[35m', 'magenta': '\033[36m', 'cinza': '\033[37m'}

print('{}'.format('<>') * 45)
print('{:^90}'.format('Tipos de Triangulos'))
print('{}'.format('<>') * 45)

a = float(input('Digite um tamanho em cm: '))
b = float(input('Digite um tamanho em cm: '))
c = float(input('Digite um tamanho em cm: '))
if (a < b + c) and (b < a + c) and (c < a + b):
    print('Com as medidas informadas {}{}{} formar um triangulo.'.format(cores['verde'], 'É POSSIVEL', cores['fim']), end=' ')
    if (a == b) and (a == c):
    # if a == b == c: -> Mesmo resultado da linha de cima!
        print('O tipo do triangulo formado é EQUILATERO!')
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print('O tipo do triangulo formado é ISÓSCELES!')
    else:
        # if a != b != c != a: -> condição para que todos termos sejam diferentes entre si!
        print('O tipo do triangulo formado é ESCALENO!')
else:
    print('Com as medidas informadas {}{}{} formar um triangulo!'.format(cores['vermelho'], 'NÃO É POSSIVEL', cores['fim']))