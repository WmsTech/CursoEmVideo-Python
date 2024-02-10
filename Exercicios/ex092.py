from datetime import date
dados = {}
print('-' * 50)
print(f'{"Previdencia Social":^50}')
print('-' * 50)
dados['nome'] = str(input('Digite o seu nome: ')).strip().title()
# dados['idade'] = (date.today().year - (int(input('Digite o seu ano de Nascimento: ')))) # Funciona, mas precisa do ano de nascimento para outro calculo
nasc = int(input('Digite o seu ano de Nascimento: '))
dados['idade'] = date.today().year - nasc
dados['carteira'] = int(input('Digite o N° da sus Carteira de Trabalho (0 se não possui): '))
if dados['carteira'] > 0:
    dados['contração'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = int(input('Digite o Salario R$ '))
    dados['aposentadoria'] = (dados['contração'] - nasc) + 35
print('-=-'*20)
for indice, valor in dados.items():
    print(f'{indice} tem o valor {valor}')
