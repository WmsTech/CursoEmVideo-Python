print('Radar 0x45fh - Radar de velocidade Rodoviario')
print('velocidade Maxima permitida -> 80 km/h. R$ 7,00 de multa para cada Km/h excedido.')
vel = int(input('Qual a velocidade o veiculo passou no radar? '))
if vel > 80:
    print('O veiculo ultrapasou o limite de velocidade!')
    print('Veiculo Multado! Valor da multa R$ {:.2f}' .format((vel - 80) * 7))
else:
    print('Velocidade dentro da maxima permitida!')
