numeros = list()
print('Digite 5 numeros e mostrarei o maior valor digitado e menor.')
maior = menor = 0
for n in range(0, 5):
    numeros.append(int(input('Digite um numero: ')))
    if n == 0:
        maior = menor = numeros[n]
        posMaior = posMenor = n
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]
print(f'Os numeros digitados foram {numeros}.')
print(f'O maior valor foi {maior} nas posições ', end='')
for pos, valor in enumerate(numeros):
    if maior == valor:
        print(f'{pos + 1}... ', end='')
print()
print(f'O menor valor foi {menor} nas posições ', end='')
for pos, valor in enumerate(numeros):
    if menor == valor:
        print(f'{pos + 1}... ', end='')
print()


