print('-' * 50)
print(f'{"MATRIZ":^50}')
print('-' * 50)
matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0,3):
        num = int(input(f'Digite um numero [{i}, {j}]: '))
        matriz[i].append(num)
print(f'Com os valores informados forma-se a seguinte matriz:')
for i in range(0, 3):
    print(f'    | ', end='')
    for j in range(0, 3):
        print(f'{matriz[i][j]} ', end='')
    print('|')
