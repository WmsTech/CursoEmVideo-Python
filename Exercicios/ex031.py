from math import ceil
print('Aviação canivets')
print('Viagens até 200 Km são R$ 0,50 o Km, acima de 200 Km são R$ 0,45.')
dist = float(input('Digite a distancia da viagem: '))
if dist > 200:
    print('Para essa distancia, o valor da passagem fica R$ {:.2f}.' .format((ceil(dist)) * 0.45))
else:
    print('Para essa distancia, o valor da passagem fica R$ {:.2f}.' .format((ceil(dist)) * 0.5))
