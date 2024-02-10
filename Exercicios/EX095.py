print('-' * 50)
print(f'{"Aproveitamento":^50}')
print('-' * 50)
jogador = dict()
gols = []
jogadores = list()
while True:
    jogador['nome'] = str(input('Digite o nome do Jogador: ')).strip().title()
    jogador['jogos'] = int(input(f'Digite a quantidade de Jogos que {jogador["nome"]} jogou:'))
    totgols = 0

    for c in range(0, jogador['jogos']):
        gol = int(input(f'Digite a quatidade de gols que {jogador["nome"]} fez no {c+1}° Jogo: '))
        gols.append(gol)
        totgols += gol
    jogador['gols'] = gols[:]
    gols.clear()
    jogador['totgols'] = totgols
    jogadores.append(jogador.copy())

    while True:
        continuar = str(input('Deseja cadastrar um novo jogador? [S/N]: ')).strip()[0]
        if continuar in 'SsNn':
            break
    if continuar in 'Nn':
        break
print('-=-'*25)
-print(f'|{"cod":^5}|{"Nome":^20}|{"Gols":^15}|{"Total":^7}|')
for pos, item in enumerate(jogadores):
   listgols = item['gols']
   print(f'|{pos + 1:^5}|{item["nome"]:^20}|{f"{listgols}":^15}|{item["totgols"]:^7}|')
print('-=-'*25)
while True:
    while True:
        continuar = str(input('Deseja ver estatistica individual de algum jogador? [S/N]: ')).strip()[0]
        if continuar in 'SsNn':
            break
    if continuar in 'Nn':
        break
    j = int(input('Qual o codigo do jogador? ')) - 1
    print('-=-'*25)
    print(f'O jogador {jogadores[j]["nome"]} jogou {jogadores[j]["jogos"]} jogos, sendo: ')
    for c in range(0, jogadores[j]['jogos']):
        print(f'   -> No {c+1}° jogo fez {jogadores[j]["gols"][c]} gols.')
    print(f'Foi um total de {jogadores[j]["totgols"]} gols.')
    print(f'Com um media de {(jogadores[j]["totgols"]/jogadores[j]["jogos"]):.1f} gols por jogo.')

'''print('-=-' * 25)
print(f'|{"cod":^5}|', end='')
for k in jogador.keys():
    print(f'{k:^20}|', end='')
print()
for k, v in enumerate(jogadores):
    print(f'|{k + 1:^5}|', end='')
    for d in v.values():
        print(f'{str(d):^20}|', end='')
    print()'''