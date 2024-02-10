print('-' * 50)
print(f'{"Cadastramento de pessoas":^50}')
print('-' * 50)
print('Digite os dados da pessoa, para o cadastramento: ')
pessoas = []
dados = list()
maiorPeso = menorPeso = 0
while True:
    dados.append(str(input('Digite o nome: ').strip().title()))
    dados.append(int(input('Peso (Kg): ')))
    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    print('-' * 40)
    print(f'{"Pessoa Cadastrada com Sucesso":^30}')
    print('-' * 40)
    while True:
        continuar = str(input('Deseja continuar adicionando pessoas? [S/N]: ')).strip()[0]
        if continuar in 'SsNn':
            break
    if continuar in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')

'''for pos , p in enumerate(pessoas):
    if pos == 0:
        maiorPeso = menorPeso = p[1]
    else:
        if p[1] > maiorPeso:
            maiorPeso = p[1]
        if p[1] < menorPeso:
            menorPeso = p[1]'''
print(f'O maior peso foi {maiorPeso} Kg, regitrado por ', end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menorPeso} Kg, registrado por ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'[{p[0]}] ', end='')

