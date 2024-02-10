print('{}'.format('<>') * 45)
print('{:^90}'.format('Somatorio'))
print('{}'.format('<>') * 45)

print('Infome um intevalo que mostrarei a soma dos numros ímpares multiplos de 3 neste intervalo!')
inicio = int(input('Digite o inicio do intervalo: '))
fim = int(input('Digite o fim do intervalo: '))

print('Considerando o intervalo de {} até {} temos os seguintes numeros ímpares multiplos de 3:'.format(inicio, fim))

s = 0
for c in range(inicio, fim + 1):
    if (c % 2 != 0) and (c % 3 == 0):
        print(c)
        s += c

print('O somatorio desses numeros é {}'.format(s))
