print('{}'.format('<>') * 45)
print('{:^90}'.format('Tabuada'))
print('{}'.format('<>') * 45)

print('Informe um numero e selecione até qual numero deseja vizualizar a sua tabuada!')
n = float(input('Digite o numero que deseja saber a sua tabuada: '))
tabu = int(input('Digite um numero inteiro que delimita a tabuada: '))

print('{}'.format('*') * 45)
print('{:^45}'.format('Tabuada de {} até o numero {}').format(n, tabu))
print('{}'.format('*') * 45)

for c in range(0, tabu + 1):
    print('{} x {:2} = {}'.format(n, c, (n * c)))
