cores = {'fim': '\033[m','branco': '\033[30m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'lilas': '\033[35m', 'magenta': '\033[36m', 'cinza': '\033[37m'}

print('{}{}{}' .format(cores['vermelho'], '-=-', cores['fim']) * 30)
print('{}{:^90}{}'.format(cores['verde'], 'WS Financeira', cores['verde']))
print('{}{}{}' .format(cores['vermelho'], '-=-', cores['fim']) * 30)
print('Programa de imprestimo facil! - Impestimos garantidos para prestações abaixo de 30% do seu salario')
casa = float(input('Digite o Valor da Casa que deseja comprar R$'))
sal = float(input('Qual o valor do seu salario R$'))
meses = int(input('Quantos meses você deseja pagar o imovel? '))

prestacao = (casa / meses)
print('Para o imovel no valor de R$ {:.2f} e o prazo de {} meses, a prestação mensal fica em R$ {:.2f}'.format(casa, meses, prestacao))

if prestacao < (sal * (0.3)):
    print('{}{}{}'.format(cores['verde'], 'Parabens! Com essas condições o seu Imprestimo foi aprovado!', cores['fim']))
else:
    print('{}{}{}'.format(cores['vermelho'], 'Desculpe, infelizmente o seu Imprestimo não foi aprovado.', cores['fim']))

