aluno = dict() # mesmo que aluno ={}
print('-' * 50)
print(f'{"Lançamento de Media Escolares":^50}')
print('-' * 50)
nome = str(input('Digite o nome do Aluno: ')).strip().title()
media = float(input(f'Digite a Media de {nome}: '))
situacao = 'Aprovado' if media >= 7 else 'Reprovado'
aluno['nome'] = nome
aluno['media'] = media
aluno['situacao'] = situacao
for indice, valor in aluno.items():
    print(f'O {indice} é igual a {valor}.')
