boletim = []
aluno =[]
nota = []

while True:
	aluno.append(str(input('Digite o Nome do Aluno:  ')).strip().title())
	nota.append(float(input('Digite a primeira nota: ')))
	nota.append(float(input('Digite a segunda nota: ')))
	aluno.append(nota[:])
	boletim.append(aluno[:])
	nota.clear()
	aluno.clear()
	print('-' * 50)
	print(f'{"Aluno Cadastrado com Sucesso":^50}')
	print('-' * 50)
	while True:
		continuar = str(input('Deseja continuar? [S/N]: ')).strip()[0]
		if continuar in 'SsNn':
			break
	if continuar in 'Nn':
		break
print(f'Foram Cadastrado {len(boletim)} Alunos.')
print('-=' * 25)
print('-' * 45)
print(f'|{"N°":^4}|{"Nome":^30}|{"Média":^7}|')
for pos, item in enumerate(boletim):
	media = (item[1][0] + item[1][1]) / 2
	print(f'|{pos + 1:^4}|{item[0]:^30}|{media:^7.2f}|')
print('-' * 45)

while True:
	while True:
		continuar = str(input('Deseja ver nota individual de algum Aluno? [S/N]: ')).strip()[0]
		if continuar in 'SsNn':
			break
	if continuar in 'Nn':
		break
	else:
		alun = int(input('Digite o Numero do aluno que deseja ver a nota: '))
		print(f'O aluno {boletim[alun - 1][0]} tem as seguintes notas {boletim[alun - 1][1]}.')

