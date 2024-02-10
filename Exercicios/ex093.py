print('-' * 50)
print(f'{"Aproveitamento":^50}')
print('-' * 50)
jogador = dict()
gols = []
jogador['nome'] = str(input('Digite o nome do Jogador: ')).strip().title()
jogador['jogos'] = int(input(f'Digite a quantidade de Jogos que {jogador["nome"]} jogou:'))
totgols = 0
for c in range(0, jogador['jogos']):
    gol = int(input(f'Digite a quatidade de gols que {jogador["nome"]} fez no {c+1}° Jogo: '))
    gols.append(gol)
    totgols += gol
jogador['gols'] = gols[:]
jogador['totgols'] = totgols
# jogador['totgols] = sum(gols) # recebe a soma sum() da lista gols. 
print('-=-'*25)
print(jogador)
print('-=-'*25)
for indice, valor in jogador.items():
    print(f'O indice {indice} tem o valor {valor}')
print('-=-'*25)
print(f'O jogador {jogador["nome"]} jogou {jogador["jogos"]} jogos, sendo: ')
for c in range(0, jogador['jogos']):
    print(f'   -> No {c+1}° jogo fez {jogador["gols"][c]} gols.')
print(f'Foi um total de {jogador["totgols"]} gols.')
print(f'Com um media de {(jogador["totgols"]/jogador["jogos"]):.1f} gols por jogo.')