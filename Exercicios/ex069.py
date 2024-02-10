print('-=-' * 30)
print(f'{"Pesquisa IBGE":^90}')
print('-=-' * 30)
print('Digite a idade e sexo de cada invidiuo para o Censo IBGE.')
qtdPessoas = maiores = qtdHomens = qtdMulheres = 0
continuar = ' '
while True:
    idade = int(input('Digite a idade: '))
    while True:
        sexo = str(input('Digite o sexo Masculino ou Feminino [M/F]: ')).strip()[0]
        if sexo in 'MmFf':
            break
    print('-' * 40)
    print('Essa pessoa foi cadastrada com Sucesso!')
    print('-' * 40)
    qtdPessoas += 1
    if sexo in 'Mm':
        qtdHomens += 1
    else:
        if idade < 20:
            qtdMulheres += 1
    if idade >= 18:
        maiores += 1
    while True:
        continuar = str(input('Deseja continuar Informando dados? [S/N] ->')).strip()[0]
        if continuar in 'SsNn':
            break
    if continuar in 'Nn':
        break
if qtdPessoas == 1:
    print(f'Foram cadastradas {qtdPessoas} pessoas.'.replace('Foram cadastradas', 'Foi cadastrada').replace('pessoas', 'pessoa'), end=' ')
    if maiores == 1:
        print(f'{maiores} pessoas são maiores de idade,'.replace('pessoas são maiores', 'pessoa é maior'), end=' ')
    else:
        print(f'{maiores} pessoas são maiores de idade,', end=' ')
    if qtdHomens == 1:
        print(f'{qtdHomens} homens foram cadastrados e'.replace('homens foram cadastrados', 'homem foi cadastrado'), end=' ')
    else:
        print(f'{qtdHomens} homens foram cadastrados e', end=' ')
    if qtdMulheres == 1:
        print(f'{qtdMulheres} mulheres têm menos de 20 anos.'.replace('mulheres têm', 'mulher tem'))
    else:
        print(f'{qtdMulheres} mulheres têm menos de 20 anos.')
else:
    print(f'Foram cadastradas {qtdPessoas} pessoas.', end=' ')
    if maiores == 1:
        print(f'{maiores} pessoas são maiores de idade,'.replace('pessoas são maiores', 'pessoa é maior'), end=' ')
    else:
        print(f'{maiores} pessoas são maiores de idade,', end=' ')
    if qtdHomens == 1:
        print(f'{qtdHomens} homens foram cadastrados e'.replace('homens foram cadastrados', 'homem foi cadastrado'), end=' ')
    else:
        print(f'{qtdHomens} homens foram cadastrados e', end=' ')
    if qtdMulheres == 1:
        print(f'{qtdMulheres} mulheres têm menos de 20 anos.'.replace('mulheres têm', 'mulher tem'))
    else:
        print(f'{qtdMulheres} mulheres têm menos de 20 anos.')