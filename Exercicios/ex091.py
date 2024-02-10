'''from random import randint
from time import sleep
from operator import itemgetter
print('-' * 50)
print(f'{"Jogo do Dado":^50}')
print('-' * 50)
jogadores = {}
ranking = []

print('Jogue o Dado, o jogador que tirar o maior valor ganha.')
for c in range(0,4):
    while True:
        jogar = int(input(f'Olá Jogador {c + 1}, jogue o Dado [Precione 1 para jogar]: '))
        if jogar == 1:
            break
    print('JOGANDO...')
    sleep(2)
    jogadores[f'jogador{c+1}'] = randint(1, 6) 
    print('-' * 20)
    print(f'Você tirou {jogadores[f"jogador{c+1}"]}')
    print('-' * 20)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*5, 'Ranking de Jogadores', '-='*5)
for pos, item in enumerate(ranking):
    print(f'{pos + 1}° Lugar - {item[0]} tirou {item[1]} no dado')'''




from random import randint
print('-=-' *15)
print(f'{"Jogo do Dado":^45}')
print('-=-' * 15)

jogadores = {}
aux = []
ranking = []
players = []
jogador = {}
for c in range(0, 4):
	int(input(f'Ola jogador {c+1}, jogue o dado (pressione 1 para jogar): '))
	jogadores[f'jogador{c +1}'] = randint(1, 6)
	print('-' * 25)
	print(f'Voce tirou {jogadores[f"jogador{c + 1}"]} no dado')
	print('-' * 25)

for k, v in jogadores.items():
	jogador['j'] = k
	jogador['dado'] = v
	aux.append(v)
	players.append(jogador.copy())
	
	
aux.sort(reverse=True)

for valor in aux:
	for item in players:
		if valor == item['dado']:
			if item['j'] not in ranking:
				jogador['j'] = item['j']
				jogador['dado'] = item['dado']
				ranking.append(jogador.copy())

for player in ranking:
	print(player)
