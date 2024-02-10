print('-' * 50)
print(f'{"MATRIZ":^50}')
print('-' * 50)
matriz = [[], [], []]
somaPares = soma3coluna = maior2linha = 0
for i in range(0, 3):
    for j in range(0,3):
        num = int(input(f'Digite um numero [{i}, {j}]: '))
        matriz[i].append(num)
print(f'Com os valores informados forma-se a seguinte matriz:')
for i in range(0, 3):
    print(f'    | ', end='')
    for j in range(0, 3):
        print(f'{matriz[i][j]} ', end='')
        if matriz[i][j] % 2 == 0:
            somaPares += matriz[i][j]

        if j == 2:
            soma3coluna += matriz[i][j]

        if i == 1:
            if matriz[i][j] > maior2linha:
                maior2linha = matriz[i][j]
    print('|')
print(f'A soma de todos os numeros para da Matriz é {somaPares}.')
print(f'A soma da 3ª coluna é {soma3coluna}')
print(f'O maior valor da 2ª linha é {maior2linha}')
    
