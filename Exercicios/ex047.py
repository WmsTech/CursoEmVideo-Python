print('{}'.format('<>') * 45)
print('{:^90}'.format('Numeros Pares'))
print('{}'.format('<>') * 45)

print('Infome um intevalo que mostrarei os numeros pares neste intervalo!')
inicio = int(input('Digite o inicio do intervalo: '))
fim = int(input('Digite o fim do intervalo: '))

print('Considerando o intervalo de {} até {} temos os seguintes numeros pares:'.format(inicio, fim))

#if inicio % 2 == 0:             # Gera menos iterações
#    for c in range(inicio, fim + 1, 2):
#        print(c)          
#else:
#    for c in range(inicio + 1, fim + 1, 2):
#        print(c)

for c in range(inicio, fim + 1):
    if c % 2 == 0:
        print(c, end=' ')
