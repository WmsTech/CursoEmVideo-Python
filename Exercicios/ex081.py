numeros = []
qtdNumeros = 0
print('Digite alguns numeros que vou trazer algumas informações.')
while True:
    # numeros.append(int(input('Digite um numero: '))) # Solução do professor
    num = int(input('Digite um numero: '))
    numeros.append(num)
    qtdNumeros += 1
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip()[0]
        if continuar in 'SsNn':
            break
    if continuar in 'Nn':
        break
print('-='*30)
# print(f'Foram digitados o total de {qtdNumeros} numeros, sendo eles {numeros}.')
print(f'Foram digitados o total de {len(numeros)} numeros, sendo eles {numeros}.')
print('-=' * 30)
backup = numeros[:]
numeros.sort(reverse=True) # Ordena a lista de forma decrescente
print(f'Os numeros digitados ordenados de forma decrescente são {numeros}.')
print('-=' * 30)
qtd5 = 0
if 5 in backup:
    print(f'O numero 5 está na lista, nas posições ', end='')
    for pos in range(0, len(backup)):
        if backup[pos] == 5:
            print(f'{pos}...', end='')
            qtd5 += 1
    print(f' sendo digitado {qtd5} vezes.')
else:
    print('O numero 5 não foi digitado, logo não está na lista.')
