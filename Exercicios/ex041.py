from datetime import date
print('{}'.format('<>') * 45)
print('{:^90}'.format('Confederação Nacional de Natação'))
print('{}'.format('<>') * 45)
nome = str(input('Olá atetla digite o seu nome: ')).strip().title().split()
nasc = int(input('Digite seu ano de nascimento: '))
idade =date.today().year - nasc

if idade  < 0:
    print('Idade Incorreta!')
elif idade <= 9:
    print('Olá {}, muito prazer! De acordo com a sua idade de {} anos, você se encaixa na categoria MIRIM!'.format(nome[0], idade))
elif idade <= 14:
    print('Olá {}, muito prazer! De acordo com a sua idade de {} anos, você se encaixa na categoria INFANTIL!'.format(nome[0], idade))
elif idade <= 19:
    print('Olá {}, muito prazer! De acordo com a sua idade de {} anos, você se encaixa na categoria JUNIOR!'.format(nome[0], idade))
elif idade <= 25:
    print('Olá {}, muito prazer! De acordo com a sua idade de {} anos, você se encaixa na categoria SENIOR!'.format(nome[0], idade))
else:
    print('Olá {}, muito prazer! De acordo com a sua idade de {} anos, você se encaixa na categoria MASTER!'.format(nome[0], idade))
