from time import sleep
cores = {'fim': '\033[m','branco': '\033[30m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'lilas': '\033[35m', 'magenta': '\033[36m', 'cinza': '\033[37m', 'preto': '\033[7:40m'}
print('{}'.format('<>') * 45)
print('{:^90}'.format('Lojas do Perigo'))
print('{}'.format('<>') * 45)
valor = float(input('Digite o valor do produto: '))

if valor < 0:
    print('{}{}{}'.format(cores['vermelho'], 'Valor incorreto!', cores['fim']))
else:
    pag = int(input('''1 - À vista dinheiro/Cheque
2 - À vista no cartão
3 - 2 X Cartão
4 - 3 X ou mais no Cartão
Selecione o metodo de pagamento: '''))

    if 1 <= pag < 5:
        if pag == 1:
            print('Para esse metodo de pagamento tem-se 10% de desconto, então o produto que custava R$ {:.2f}, fica no valor de R$ {:.2f}.'.format(valor, (valor - (valor * 0.1))))
        elif pag == 2:
            print('Para esse metodo de pagamento tem-se 5% de desconto, então o produto que custava R$ {:.2f}, fica no valor de R$ {:.2f}.'.format(valor, (valor - (valor * 0.05))))
        elif pag == 3:
            print('Para esse metodo de pagamento não tem desconto, então o produto que custa R$ {:.2f}, e as parcelas ficam no valor de R$ {:.2f}.'.format(valor, (valor / 2)))
        else:
            parc = int(input('Quantas vezes será parcelado? '))
            print('Para esse metodo de pagamento tem-se acrescimo de 20%, então o produto que custava R$ {:.2f}, fica no valor de R$ {:.2f}, e as parcelas ficam no valor de R$ {:.2f}.'.format(valor, (valor + (valor * 0.2)), (valor + (valor * 0.2)) / parc))
    else:
        print('Forma de Pagamento Invalida, tente novamente!')