
qtd = int(input('Digite a quantidade de pessoas: '))
peso = 0
pesado = 0 
leve = 0
for pessoas in range(1, qtd + 1):
    peso = float(input(' Digite o peso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        pesado = leve = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso

print('Foi informado o peso de {} pessoas e o maior peso foi {:.1f}Kg e o menor foi {:.1f}Kg.'.format(qtd, pesado, leve))
