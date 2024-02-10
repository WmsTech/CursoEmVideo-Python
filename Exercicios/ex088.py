from random import randint
from time import sleep
print('-' * 50)
print(f'{"PALPITES MEGA SENA":^50}')
print('-' * 50)
palpites = []
jogo = []
qtdjogos = int(input('Quantos jogos você quer gerar? '))
for j in range(0, qtdjogos):
    for escolha in range(0, 6):
        r = randint(1, 60)
        if r not in jogo:
            jogo.append(r)
    palpites.append(jogo[:])
    jogo.clear()
print(f'Para {qtdjogos} jogos tenho os seguinte palpites: ')
for pos , p in enumerate(palpites):
    sleep(0.75)
    p.sort()
    print(f'{pos + 1}° jogo - {p}')
    