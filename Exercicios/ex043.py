from time import sleep
cores = {'fim': '\033[m','branco': '\033[30m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'lilas': '\033[35m', 'magenta': '\033[36m', 'cinza': '\033[37m', 'preto': '\033[7:40m'}
print('{}'.format('<>') * 45)
print('{:^90}'.format('Calculadora de IMC'))
print('{}'.format('<>') * 45)

print('Informe os valores solicitados e lhe será apresentado o seu IMC!')
peso = float(input('Informe o seu peso em Kg: '))
altura = float(input('informe a sua altura em metros: '))
imc = peso / (altura ** 2)
print('Calculando...')
sleep(2)
print('Com os valores informados o seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('Esse IMC corresponde a faixa {}{}{}'.format(cores['amarelo'], 'ABAIXO DO PESO', cores['fim']))
elif 18.5 <= imc <= 25:
    print('Esse Imc corresponde a faixa de {}{}{}'.format(cores['verde'], 'PESO IDEAL',cores['fim']))
elif 25 < imc <= 30:
    print('Esse Imc corresponde a faixa de {}{}{}'.format(cores['amarelo'], 'SOBREPESO',cores['fim']))
elif 30 < imc <= 40:
    print('Esse Imc corresponde a faixa de {}{}{}'.format(cores['vermelho'], 'OBESIDADE',cores['fim']))
else:
    print('Esse Imc corresponde a faixa de {}{}{}'.format(cores['preto'], 'OBESIDADE MORBIDA',cores['fim']))