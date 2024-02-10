from time import sleep
print('{}'.format('<>') * 45)
print('{:^90}'.format('Progressão Aritmetica'))
print('{}'.format('<>') * 45)
print('Informe dados e formarei um Progressão Aritmetica!')
a1 = float(input('Digite o primeiro termo a Progressão: '))
r = float(input('Digite a Razão entre os termos da Progressão: '))
termos = int(input('Digite a quantidade de Termos da progressão: '))
pa = 0
print('Dado que o primeiro termo sendo {} e a razão {}, a Progressão Aritmerica formada é:'.format(a1, r))
sleep(1)
print('{} '.format(a1), end=' ')
sleep(1)
for c in range(2, termos + 1):
    pa = a1 + (c - 1) * r
    print('{} '.format(pa), end=' ')
    sleep(1)
