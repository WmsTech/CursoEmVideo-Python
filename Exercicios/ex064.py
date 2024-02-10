n = 0
cont = 0
soma = 0
n = int(input('Digite um numero inteiro: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero inteiro: '))
print('Foram digitados {} numeros e a soma deles é {}'.format(cont, soma))
print('[>>> Fim de Programa <<<<]')
