numeros = []
print('-' * 50)
print(f'{"Cadastramento de numeros":^50}')
print('-' * 50)
print('Digite numeros para serem armazenado, numeros repetidos não serão armazenados!')
while True:
    num = int(input('Digite um numero: '))
    if num not in numeros:
        numeros.append(num)
        print('-' * 30)
        print(f'{"Numero Cadastrado com sucesso":^30}')
        print('-' * 30)
    else:
        print('-' * 55)
        print(f'{"Numero duplicado e já cadastrado! Digite Novo numero":^30}')
        print('-' * 55)
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip()[0]
        if continuar in 'SsNn':
            break
    if continuar in 'Nn':
        break
numeros.sort()
print('*' * 70)
print(f'Os numeros cadastrados em ordem crescente são {numeros}')
