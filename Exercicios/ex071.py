print('-=-' * 30)
print(f'{"Banco Tchurusbangos Tchurusbagos":^90}')
print('-=-' * 30)
resposta = ' '
total = cedula = 0
nota = 50
while True:
    valor = int(input('Digite o valor em R$ que deseja sacar: '))
    print(f'O saque de R$ {valor:.2f} vai se dado por:')
    while True:
        if valor >= nota:    
            valor -= nota
            cedula += 1
        else:
            if cedula > 0:
                print(f'{cedula} notas de R$ {nota}')
            if nota == 50:
                nota = 20
            elif nota == 20:
                nota = 10
            elif nota == 10:
                nota = 1
            cedula = 0
            if valor == 0:
                break
    cedula = 0
    nota = 50    
    '''cedula50 = valor // 50
    resto = valor % 50
    cedula20 = resto // 20
    resto = resto % 20
    cedula10 = resto // 10
    resto = resto % 10
    cedula1 = resto // 1'''
    '''print('=' * 30)
    print(f'Para R$ {valor:.2f}, será sacado: \n{cedula50} cedulas de R$ 50 \n{cedula20} cedulas de R$ 20 \n{cedula10} cedulas de R$ 10  \n{cedula1} cedulas de R$ 1')
    print('=' * 30)'''

    while True:
        resposta = str(input('Deseja Sacar outro valor? [S/N] -> '))
        if resposta in 'SsNn':
            break
    if resposta in 'Nn':
        break
print(' * ' * 20)
print('O banco Tchurusbangos Tchurusbagos Agradece a Preferencia!')
print(' * ' * 20)
