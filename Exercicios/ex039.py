from datetime import date
cores = {'fim': '\033[m','branco': '\033[30m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'lilas': '\033[35m', 'magenta': '\033[36m', 'cinza': '\033[37m'}

print('{}'.format('<>') * 45)
print('{:^90}'.format('Alistamento Militar'))
print('{}'.format('<>') * 45)
nasc = int(input('Em que ano você nasceu? '))
sexo = str(input('Qual o seu sexo? Masculino (M)/Feminino (F) ')).strip().upper()
atual = date.today().year
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, (atual - nasc), atual))

if sexo == 'F':
    print('Você não tem Alistamento Militar obrigatorio!')
elif (atual - nasc) < 18:
    print('Você ainda não tem idade para se alistar, seu alistamento será em {}'.format(nasc + 18))
elif (atual - nasc) > 18:
    print('Você está com o seu alistamento atrasado, seu ano de alistamento foi {}'.format(nasc + 18))
else:
    print('O ano de {} é o ano do seu alistamento, se aliste IMENDIATAMENTE!'.format(atual))
