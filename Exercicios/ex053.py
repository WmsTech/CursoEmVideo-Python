cores = {'fim': '\033[m','branco': '\033[30m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'lilas': '\033[35m', 'magenta': '\033[36m', 'cinza': '\033[37m', 'preto': '\033[7:40m'}

print('{}'.format('<>') * 45)
print('{:^90}'.format('PALÍNDROMO'))
print('{}'.format('<>') * 45)
print('{}{}{}'.format(cores['amarelo'], 'Palindromo são frase que tem a mesma forma escrita inversamente.', cores['fim']))

frase = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(frase)
tamanho = len(junto)
n = len(frase)
caractere = len(frase[n - 1])
invertido = ''

invertido = junto[::-1] # Solução Ninja

'''for letra in range(tamanho - 1, -1, -1): # Forma de resolução Professor
    invertido += frase[letra]'''


'''for c in range(n - 1, -1, -1):   Minha forma de Resolução. 
    for letra in range(caractere - 1, -1, -1):
        invertido += frase[c][letra]'''

print('Voce escreveu {} e invertido fica {}.'.format(junto, invertido))

if junto == invertido:
    print('É um PALÍNDROMO!')
else:
    print('NÃO é um PALÍNDROMO!')
    