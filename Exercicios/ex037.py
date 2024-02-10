cores = {'fim': '\033[m','branco': '\033[30m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'lilas': '\033[35m', 'magenta': '\033[36m', 'cinza': '\033[37m'}

print('{}{}{}' .format(cores['azul'], '-=-', cores['fim']) * 30)
print('{}{:^90}{}'.format(cores['verde'], 'Conversor de Numeros', cores['verde']))
print('{}{}{}' .format(cores['azul'], '-=-', cores['fim']) * 30)
print('Converta um numero intero para binario, octal ou hexadecimal')

n = int(input('Digite um numero inteiro: '))
print('Opções de Conversão: ', '\n1 - Binario', '\n2 - Octal', '\n3 - Hexadecimal')
conversao = int(input('Escolha a conversão: '))
    
if conversao == 1:
    print('O numero {}{}{} convertido para Binario é {}{}{}.'.format(cores['amarelo'], n, cores['fim'], cores['vermelho'], bin(n)[2:], cores['fim']))
elif conversao == 2:
    print('O numero {}{}{} convertido para Octal é {}{}{}'.format(cores['amarelo'], n, cores['fim'], cores['vermelho'], oct(n)[2:], cores['fim']))
elif conversao == 3:
    print('O numero {}{}{} convertido para Hexadecimal é {}{}{}'.format(cores['amarelo'], n, cores['fim'], cores['vermelho'], hex(n)[2:], cores['fim']))
else:
    print('{}{}{}'.format(cores['vermelho'], 'Opção invalida', cores['fim']))
