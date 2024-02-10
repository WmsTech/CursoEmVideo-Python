from time import sleep
print('{}'.format('<>') * 45)
print('{:^90}'.format('Contagem Regressiva para Fogos de Artificios'))
print('{}'.format('<>') * 45)

print('Atenção, preparar para a contagem!')
sleep(3)

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print('{}'.format('*') * 45)
print('{:^45}'.format('FOGOS'))
print('{}'.format('*') * 45)
    