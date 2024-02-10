numeros = []
pares = list()
impares = []
print('Digite alguns numeros e vou apresentar sem os numeros pares e impares digitados.')
while True:
    '''num = int(input('Digite um numero: '))
    numeros.append(num)'''
    numeros.append(int(input('Digite um numero: ')))
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip()[0]
        if continuar in 'SsNn':
            break
    if continuar in 'Nn':
        break
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

'''while True:
    num = int(input('Digite um numero: '))
    numeros.append(num)
    qtdNumeros += 1
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip()[0]
        if continuar in 'SsNn':
            break
    if continuar in 'Nn':
        break'''

print('-=' * 50)
print(f'Foram digitados {len(numeros)} numeros, sendo eles {numeros}.')
print(f'Os numeros pares digitados foram {pares}')
print(f'Os numeros ímpares digitados foram {impares}')


