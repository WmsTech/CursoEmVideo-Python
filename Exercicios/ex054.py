from datetime import date
cores = {'fim': '\033[m','branco': '\033[30m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'lilas': '\033[35m', 'magenta': '\033[36m', 'cinza': '\033[37m', 'preto': '\033[7:40m'}
print('{}'.format('<>') * 45)
print('{:^90}'.format('MAIORIDADE'))
print('{}'.format('<>') * 45)
print('{}{}{}'.format(cores['amarelo'], 'Informe uma data de nascimento para identificar se corresponde ao um individuo, maior ou menor de idade (MAIORIDADE >= 21).', cores['fim']))

qtd = int(input('Digite a quantidade de datas de Nascimento que serão informada: '))
maior = 0
menor = 0
for c in range(1, qtd + 1):
    print('{}'.format('-') * 30)
    print('{:^30}'.format('{}ª Data de Nascimento'.format(c)))
    print('{}'.format('-') * 30)
    dia = int(input('Digite o dia do nascimento: '))
    mes = int(input('Digite o mes do nascimento: '))
    ano = int(input('Digite o ano do nascimento: '))

    if (date.today().year - ano > 21) or (dia <= date.today().day) and (mes <= date.today().month) and (date.today().year - ano == 21):
       maior += 1
       print('{}'.format('-> Individuo MAIOR de Idade <-'))
    else:
        menor += 1
        print('{}'.format('-> Individuo MENOR de Idade <-'))

if maior == 1:
    if menor == 1: 
        print('Das datas de nascimentos informadas, {} pessoas são MAIORES de idade e {} MENORES.'.format(maior, menor).replace('pessoas são MAIORES', 'pessoa é MAIOR').replace('MENORES', 'MENOR'))
    else:
        print('Das datas de nascimentos informadas, {} pessoas são MAIORES de idade e {} MENORES.'.format(maior, menor).replace('pessoas são MAIORES', 'pessoa é MAIOR'))
else:
    if menor == 1: 
        print('Das datas de nascimentos informadas, {} pessoas são MAIORES de idade e {} MENORES.'.format(maior, menor).replace('MENORES', 'MENOR'))
    else:
        print('Das datas de nascimentos informadas, {} pessoas são MAIORES de idade e {} MENORES.'.format(maior, menor))
