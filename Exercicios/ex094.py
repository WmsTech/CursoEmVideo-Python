print('-' * 50)
print(f'{"Cadastramento":^50}')
print('-' * 50)
dados = {}
pessoas = []
print('Digite dados da pessoa para o cadastramento no banco de dados.')
while True:
    dados['nome'] = str(input('Digite o NOME da pessoa: ')).strip().title()
    while True:
        dados['sexo'] = str(input(f'Digite o SEXO de {dados["nome"]} [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
    dados['idade'] = int(input(f'Digite a IDADE de {dados["nome"]}: '))
    pessoas.append(dados.copy())
    print('-=-' * 15)
    while True:
        continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).strip()[0]
        if continuar in 'SsNn':
            break
    if continuar in 'Nn':
        break
print('-=-' * 25)
print(f'- Foram cadastradas {len(pessoas)} pessoas.')
totidade = 0
mulheres = []
for item in pessoas:
    totidade += item['idade']
    if item['sexo'] == 'F':
        mulheres.append(item['nome'])
media = totidade / len(pessoas)
print(f'- A media de idade de todas as pessoas cadastras é {media:.1f} anos.')
print(f'- As mulheres cadastradas são {mulheres}.')
acimaMedia = []
print(f'- As pessoas com a idade acima da media são: ')
for item in pessoas:
    if item['idade'] > media:
        for k, v in item.items():
            print(f'    {k} = {v}', end='')
        print()
print('[>>>> FIM DE PROGRAMA <<<<]')