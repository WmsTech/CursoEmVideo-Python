qtdPessoas = int(input('Digite a quantidade de pessoas que será informada: '))

media = 0
velho = 0
maisVelho = ''
mulher = 0
contMasc = 0
contFem = 0

for c in range(1, qtdPessoas + 1):
    print('{}'.format('-') * 30)
    print('{:^30}'.format('Dados da {}ª Pessoa'.format(c)))
    print('{}'.format('-') * 30)
    nome = str(input('Digite o seu nome: ')).strip().title()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo, Masculino (M) ou Feminino (F): ')).strip().upper()

    media += idade
    if sexo == 'M':
        contMasc += 1
        if idade > velho:
            velho = idade
            maisVelho = nome
    else:
        contFem += 1
        if idade < 20:
            mulher += 1

print('A media de idade das {} pessoas é {:.1f}, sendo elas {} Homens e {} Mulheres.'.format(qtdPessoas, (media / qtdPessoas), contMasc, contFem))
print('O homem mais velho é {} que tem {} anos, e tem {} mulheres com menos de 20 anos.'.format(maisVelho, velho, mulher))
